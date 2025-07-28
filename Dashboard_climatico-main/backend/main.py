from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
import requests
from datetime import datetime, timedelta

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

cities = {
    "Madrid": (40.4168, -3.7038),
    "Valencia": (39.4699, -0.3763),
    "Barcelona": (41.3874, 2.1686),
    "Sevilla": (37.3886, -5.9823),
    "Leon": (42.5987, -5.5671),
    "Oviedo": (43.3619, -5.8494),
    "Badajoz": (38.8794, -6.9707),
    "Santiago de Compostela": (42.8782, -8.5448),
}


@app.get("/clima")
def obtener_clima(
    ciudad: str = Query(...),
    fecha_inicio: Optional[str] = Query(None),
    fecha_fin: Optional[str] = Query(None)
):
    ciudad_normalizada = ciudad.strip().lower()
    ciudad_encontrada = None

    for c in cities:
        if c.lower() == ciudad_normalizada:
            ciudad_encontrada = c
            break

    if ciudad_encontrada is None:
        return {"error": "Ciudad no válida"}

    lat, lon = cities[ciudad_encontrada]

    # Manejo de fechas: por defecto, últimos 30 días
    try:
        if fecha_inicio and fecha_fin:
            start = datetime.strptime(fecha_inicio, "%Y-%m-%d").strftime("%Y%m%d")
            end = datetime.strptime(fecha_fin, "%Y-%m-%d").strftime("%Y%m%d")
        else:
            end = (datetime.now() - timedelta(days=1)).strftime("%Y%m%d")
            start = (datetime.now() - timedelta(days=30)).strftime("%Y%m%d")
    except ValueError:
        return {"error": "Formato de fecha inválido. Usa YYYY-MM-DD"}

    base_url = "https://power.larc.nasa.gov/api/temporal/daily/point"
    params = {
        "parameters": "T2M,RH2M,PRECTOTCORR",
        "start": start,
        "end": end,
        "format": "JSON",
        "community": "AG",
        "latitude": lat,
        "longitude": lon,
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()["properties"]["parameter"]
        return {"ciudad": ciudad_encontrada, "data": data}
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return {"error": f"HTTP error: {http_err}"}
    except Exception as err:
        print(f"Other error: {err}")
        return {"error": f"Other error: {err}"}
