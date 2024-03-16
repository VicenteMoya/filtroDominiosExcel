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

Las contribuciones son bienvenidas. Si tienes una sugerencia para mejorar este script, no dudes en abrir una incidencia (issue) o un pull request.

## Licencia

Este proyecto está licenciado bajo la Licencia Creative Commons Attribution-NonCommercial (CC BY-NC) - ver el [enlace de la licencia](https://creativecommons.org/licenses/by-nc/4.0/) para más detalles. Eres libre de compartir y adaptar el material siempre que reconozcas la autoría y no lo utilices para fines comerciales.

## Autor

Este script fue creado por [VicenteMoya](https://github.com/VicenteMoya). Si encuentras este script útil, considera darle una estrella al repositorio en GitHub.

---

