import pandas as pd
import requests
from datetime import datetime, timedelta
from time import sleep

# Coordenadas de las ciudades:
cities = {
    "A Coruña": (43.37012643, -8.39114853),
    "Albacete": (38.99588053, -1.85574745),
    "Alicante": (38.34548705, -0.4831832),
    "Almería": (36.83892362, -2.46413188),
    "Ávila": (40.65586958, -4.69771277),
    "Badajoz": (38.87874339, -6.97099704),
    "Barcelona": (41.38424664, 2.17634927),
    "Bilbao": (43.25721957, -2.92390606),
    "Burgos": (42.34113004, -3.70419805),
    "Cáceres": (39.47316762, -6.37121092),
    "Cádiz": (36.52171152, -6.28414575),
    "Castellón de la Plana": (39.98640809, -0.03688142),
    "Ciudad Real": (38.98651781, -3.93131981),
    "Córdoba": (37.87954225, -4.78032455),
    "Cuenca": (40.07653762, -2.13152306),
    "Girona": (41.98186075, 2.82411899),
    "Granada": (37.17641932, -3.60001883),
    "Guadalajara": (40.63435548, -3.16210273),
    "Huelva": (37.26004113, -6.95040588),
    "Huesca": (42.14062739, -0.40842276),
    "Jaén": (37.7651913, -3.7903594),
    "Las Palmas de Gran Canaria": (28.099378545, -15.413368411),
    "León": (42.59912097, -5.56707631),
    "Lleida": (41.61527355, 0.62061934),
    "Logroño": (42.46644945, -2.44565538),
    "Lugo": (43.0091282, -7.55817392),
    "Madrid": (40.40841191, -3.68760088),
    "Málaga": (36.72034267, -4.41997511),
    "Murcia": (37.98436361, -1.1285408),
    "Ourense": (42.33654919, -7.86368375),
    "Oviedo": (43.36232165, -5.84372206),
    "Palencia": (42.0078373, -4.53460106),
    "Palma": (39.57114699, 2.65181698),
    "Pamplona": (42.814102, -1.6451528),
    "Santa Cruz de Tenerife": (28.463597, -16.251846),
    "Pontevedra": (42.43381442, -8.64799018),
    "Salamanca": (40.96736822, -5.66538084),
    "San Sebastián": (43.318333, -1.981233),
    "Santander": (43.462305, -3.809980),
    "Segovia": (40.948177, -4.118493),
    "Sevilla": (37.3886, -5.9823),
    "Soria": (41.766976, -2.470976),
    "Tarragona": (41.118882, 1.24449),
    "Teruel": (40.344303, -1.106831),
    "Toledo": (39.8628316, -4.027323),
    "Valencia": (39.4699, -0.3763),
    "Valladolid": (41.652257, -4.724513),
    "Vitoria-Gasteiz": (42.8466915, -2.6726673),
    "Zamora": (41.50365, -5.744829),
    "Zaragoza": (41.648823, -0.889085)
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