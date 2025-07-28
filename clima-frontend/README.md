# 🌦️ Dashboard Climático

Una aplicación interactiva que permite visualizar datos climáticos históricos para distintas ciudades de España. El usuario puede seleccionar una ciudad, una variable (temperatura, humedad, precipitación) y el modo de visualización (gráfico o tabla), así como elegir entre los últimos 30 días o un rango de fechas personalizado.

---

## 🚀 Tecnologías utilizadas

### 🔧 Backend

- **FastAPI** (Python)
- **API de la NASA POWER** para datos meteorológicos históricos
- **Pandas** para procesamiento de datos

### 🎨 Frontend

- **React** (con Vite)
- **Recharts** para visualización interactiva de gráficos
- **Framer Motion** para animaciones suaves
- **CSS personalizado** para un diseño atractivo y accesible

---

## 🧠 Funcionalidades principales

- Selección de ciudad: Madrid, Sevilla, Barcelona, etc.
- Variables disponibles:
  - Temperatura (T2M)
  - Humedad relativa (RH2M)
  - Precipitación (PRECTOTCORR)
- Vista en gráfico o tabla
- Selección de rango de fechas o últimos 30 días
- Animaciones durante la carga de datos

---

## 👨‍💻 Autores

### 🧑 Carlos "Tuto" Curiel

- Rol: **Frontend Developer & UI/UX**
- Encargado del desarrollo en React, animaciones, modularización del código, estilos responsive y experiencia de usuario.
- [GitHub](https://github.com/AuthorGG) | [LinkedIn](https://www.linkedin.com/in/carlos-curiel-66bb1b105/)

### 👩‍💻 Luisa

- Rol: **Data Analyst & Backend Developer**
- Encargada de la integración con la API de la NASA, tratamiento de datos con Pandas, lógica de consulta por ciudad, fechas y variables.
- [GitHub de Luisa](https://github.com/Lui360)

---

## 📦 Instalación y uso

1. Clona el repositorio:

```bash
git clone https://github.com/tu-usuario/dashboard-climatico.git
cd dashboard-climatico
```

2. Instala dependencias del frontend y backend:

```bash
cd clima-frontend
npm install

cd ../Dashboard_climatico-main/backend
pip install -r requirements.txt
```

3. Inicia ambos servidores en paralelo desde el frontend:

```bash
npm run start
```

> Esto lanzará el backend en `http://127.0.0.1:8000` y el frontend en `http://localhost:5173`.

---

## 📝 Notas finales

Este proyecto ha sido desarrollado como ejercicio de aprendizaje y colaboración multidisciplinar entre programación web y análisis de datos climáticos.  
Esperamos que te resulte útil y lo disfrutes tanto como nosotros creándolo. 😊
