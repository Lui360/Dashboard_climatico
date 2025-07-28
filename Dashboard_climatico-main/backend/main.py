from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import requests 
from datetime import datetime, timedelta
import pandas as pd

app = FastAPI()

#CORS para React 

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

cities={
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
def obtener_clima(ciudad: str = Query(...)):
    ciudad_normalizada = ciudad.strip().lower()
    ciudad_encontrada = None

    for c in cities:
        if c.lower() == ciudad_normalizada:
            ciudad_encontrada = c
            break

    if ciudad_encontrada is None:
        return {"error": "Ciudad no válida"}

    lat, lon = cities[ciudad_encontrada]

    base_url = "https://power.larc.nasa.gov/api/temporal/daily/point"
    params = {
        "parameters": "T2M,RH2M,PRECTOTCORR",
        "start": "19840101",
        "end": (datetime.now() - timedelta(days=3)).strftime("%Y%m%d"),
        "format": "JSON",
        "community": "AG",
        "latitude": lat,
        "longitude": lon,
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()["properties"]["parameter"]
        return {"ciudad": ciudad, "data": data}
    except Exception as e:
        return {"error": str(e)}