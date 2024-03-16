>[!TIP]
>Descargando/clonando el repositorio entero, las librerias están ya incluidas

# Filtro Dominios Excel 💻

Este script permite a los usuarios filtrar una lista de dominios desde un archivo Excel y clasificarlos en base a su código de respuesta HTTP.

## Características ⭐

- Filtrar dominios que devuelven códigos de estado HTTP 200, redirecciones (300-399) y errores (400+).
- Genera un archivo Excel con dominios clasificados en hojas separadas según su código de estado.
- Proporciona un archivo Excel de prueba (`testDominios.xlsx`) para un uso rápido y fácil.

## Uso 🔨

Para utilizar el script, sigue estos pasos:

1. Asegúrate de tener Python (3.8 o superior) instalado en tu sistema.
2. Instala las librerías necesarias ejecutando: `pip install pandas requests`.
3. Si deseas usar el archivo Excel de prueba provisto:
   - Escribe los dominios en la primera columna del archivo `testDominios.xlsx`, comenzando desde la segunda fila.
   - Ejecuta el script con el comando `python main.py`.
4. Si deseas usar tu propio archivo Excel:
   - Asegúrate de que tu archivo tenga una columna encabezada con 'Enlace' y que los dominios estén listados debajo de este encabezado.
   - Modifica la variable `file_path` en el script para que contenga la ruta completa de tu archivo Excel.
   - Ejecuta el script con el comando `python main.py`.

>[!WARNING]
>Este script requiere las siguientes librerías para su ejecución:
>- pandas
>- requests
>- openpyxl

Asegúrate de instalarlas antes de ejecutar el script.

## Contribuciones

Las contribuciones son bienvenidas. Si tienes una sugerencia para mejorar este script, no dudes en abrir un problema (issue) o una solicitud de extracción (pull request).

## Licencia

Este proyecto está licenciado bajo [insertar tipo de licencia], lo que significa que puedes modificar y distribuir libremente el código fuente siempre que respetes los términos de la licencia.

## Autor

Este script fue creado por [VicenteMoya](https://github.com/VicenteMoya). Si encuentras este script útil, considera darle una estrella al repositorio en GitHub.

---

