🌍 Dashboard Climático de Ciudades Españolas (NASA POWER):

Este proyecto muestra un dashboard interactivo con datos climáticos diarios (temperatura, humedad y precipitación) desde 1984 hasta hoy, extraídos en tiempo real de la API NASA POWER, para varias ciudades españolas.

📌 Ciudades incluidas:
|      Ciudad       |      Ciudad       |      Ciudad       |      Ciudad       |
|:-----------------:|:-----------------:|:-----------------:|:-----------------:|
| A Coruña          | Alicante          | Ciudad Real       | Córdoba           |
| Albacete          | Almería           | Cuenca            | Barcelona         |
| Bilbao            | Girona            | Burgos            | Cáceres           |
| Granada           | Cádiz             | Castellón de la Plana | Guadalajara     |
| Jaén              | León              | Las Palmas de Gran Canaria | Huelva       |
| Lugo              | Lleida            | Huesca            | Madrid            |
| Logroño           | Málaga            | Murcia            | Ourense           |
| Oviedo            | Palencia          | Pamplona          | Palma             |
| Pontevedra        | Salamanca         | San Sebastián     | Santa Cruz de Tenerife |
| Santander         | Segovia           | Sevilla           | Soria             |
| Tarragona         | Teruel            | Toledo            | Valencia          |
| Valladolid        | Vitoria-Gasteiz   | Zamora            | Zaragoza          |

📊 Variables climáticas:
- Temperatura media (°C)
- Humedad relativa (%)
- Precipitación diaria (mm)

🧪 Tecnologías usadas:
- Python
- Streamlit — dashboard interactivo
- Plotly — visualizaciones
- NASA POWER API — fuente de datos
- Pandas — análisis de datos

📘 Instalación y uso:
- En la wiki hay una guía de instalación y ejecución del dashboard climático paso a paso.

📝 Archivos principales:
- descargar_datos_nasa.py	- Script para descargar datos desde la API de NASA POWER
- app.py -	Dashboard en Streamlit
- requirements.txt - Librerías necesarias para el proyecto
- .gitignore -	Archivos y carpetas excluidas del repositorio
