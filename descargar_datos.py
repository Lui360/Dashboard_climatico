import pandas as pd
import requests
from datetime import datetime
from time import sleep

# Coordenadas de las ciudades:
cities = {
    "Madrid": (40.4168, -3.7038),
    "Valencia": (39.4699, -0.3763),
    "Barcelona": (41.3874, 2.1686),
    "Sevilla": (37.3886, -5.9823),
    "Leon": (42.5987, -5.5671),
    "Oviedo": (43.3619, -5.8494),
    "Badajoz": (38.8794, -6.9707),
    "Santiago de Compostela": (42.8782, -8.5448)
}

# Configuración de la API
base_url = "https://power.larc.nasa.gov/api/temporal/daily/point"
params_base = {
    "parameters": "T2M,RH2M,PRECTOTCORR",
    "start": "19840101",
    "end": datetime.now().strftime("%Y%m%d"),
    "format": "JSON",
    "community": "AG",
}

# Descarga de datos
all_data = []

for city, (lat, lon) in cities.items():
    params = params_base.copy()
    params["latitude"] = lat
    params["longitude"] = lon
    print(f"Descargando datos para {city}...")

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()["properties"]["parameter"]
        fechas = data["T2M"].keys()
        df = pd.DataFrame({
            "city": city,
            "date": pd.to_datetime(list(fechas)),
            "temperature_C": list(data["T2M"].values()),
            "humidity_%": list(data["RH2M"].values()),
            "precipitation_mm": list(data["PRECTOTCORR"].values())
        })
        all_data.append(df)
    except Exception as e:
        print(f"Error en {city}: {e}")
    sleep(1.5)

# Guardar en CSV
df_all = pd.concat(all_data)
df_all.to_csv("nasa_clima_espana_1984_hoy.csv", index=False)
print("✅ Datos guardados en 'nasa_clima_espana_1984_hoy.csv'")