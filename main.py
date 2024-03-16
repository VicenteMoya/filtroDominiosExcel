
## Autor: https://github.com/VicenteMoya

import pandas as pd
import requests
import openpyxl
from requests.exceptions import RequestException
import time

# Función para obtener el código de respuesta HTTP
def get_http_status(domain,index):
    try:
        response = requests.head(domain, allow_redirects=False, timeout=10)
        return response.status_code
    except RequestException as e:
        print(f"{index} Error al procesar {domain}: {e}")
        return None

# Leer el archivo Excel
file_path = "testDominios.xlsx"

#Si tienes el archivo excel en otra ubicación, descomenta esta línea y comenta la anterior:
#file_path = "C:/.../{tuArchivo}.xlsx" # Ruta del archivo con dominios
df = pd.read_excel(file_path)

# Extraer la lista de dominios
domains = df['Enlace'][1:]  # La columna tendrá que encabezarse primero con 'Enlace'
                            # Leerá todos los dominios escritos en ella

# Iniciar el cronómetro
start_time = time.time()

# Diccionario para almacenar los códigos de estado
domain_status = {}

# Verificar el código de estado para cada dominio
for index, domain in enumerate(domains, start=1):  # Comienza el conteo desde 1
    status = get_http_status(domain, index)
    domain_status[domain] = status


# Detener el cronómetro
end_time = time.time()

# Calcular el tiempo total de ejecución
total_time = end_time - start_time
print(f"Tiempo total de ejecución: {total_time} segundos")

# Clasificar los dominios
dominios_redireccion = {d: s for d, s in domain_status.items() if s is not None and s >= 300 and s < 400}
dominios_error = {d: s for d, s in domain_status.items() if s is not None and s >= 400}
dominios_ok = {d: s for d, s in domain_status.items() if s == 200}

# Crear dos DataFrames para los dominios clasificados
df_redireccion = pd.DataFrame(list(dominios_redireccion.items()), columns=['Dominio', 'Estado HTTP'])
df_error = pd.DataFrame(list(dominios_error.items()), columns=['Dominio', 'Estado HTTP'])
df_ok = pd.DataFrame(list(dominios_ok.items()), columns=['Dominio', 'Estado HTTP'])

# Guardar en Excel
with pd.ExcelWriter('dominios_clasificados.xlsx') as writer:
    df_redireccion.to_excel(writer, sheet_name='Redirecciones', index=False)
    df_error.to_excel(writer, sheet_name='Errores', index=False)
    df_ok.to_excel(writer, sheet_name='Ok200', index=False)
