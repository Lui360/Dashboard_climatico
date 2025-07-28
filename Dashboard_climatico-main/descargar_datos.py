import pandas as pd
import requests
from datetime import datetime, timedelta
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
    "end": (datetime.now() - timedelta(days=3)).strftime("%Y%m%d"),
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
            "Ciudad": city,
            "Fecha": pd.to_datetime(list(fechas)),
            "Temperatura (°C)": list(data["T2M"].values()),
            "Humedad relativa (%)": list(data["RH2M"].values()),
            "Precipitación (mm)": list(data["PRECTOTCORR"].values())
        })
        all_data.append(df)
    except Exception as e:
        print(f"Error en {city}: {e}")
    sleep(1.5)

# Guardar en CSV
df_all = pd.concat(all_data)
df_all.to_csv("nasa_clima_espana_1984_hoy.csv", index=False)
print("Datos guardados en 'nasa_clima_espana_1984_hoy.csv'")


# Rango de últimos 30 días
end = datetime.today()
start = end - timedelta(days=30)

start_str = start.strftime("%Y%m%d")
end_str = end.strftime("%Y%m%d")

url = f"https://power.larc.nasa.gov/api/temporal/daily/point?parameters=T2M,PRECTOTCORR, RH2M&start={start_str}&end={end_str}&format=JSON&community=AG&latitude=40.4168&longitude=-3.7038"