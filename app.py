import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar datos
#@st.cache_data
def load_data():
    df = pd.read_csv("nasa_clima_espana_1984_hoy.csv", parse_dates=["date"])
    return df

df = load_data()

# Título
st.title("🌍 Dashboard Climático de Ciudades Españolas (NASA POWER)")
st.markdown("Datos diarios desde **1984 hasta hoy** para temperatura, humedad y precipitaciones. Fuente: [NASA POWER](https://power.larc.nasa.gov/)")

# Sidebar
st.sidebar.header("Opciones")
selected_city = st.sidebar.selectbox("Selecciona una ciudad", sorted(df["city"].unique()))
selected_variable = st.sidebar.selectbox("Variable a visualizar", {
    "temperature_C": "Temperatura (°C)",
    "humidity_%": "Humedad relativa (%)",
    "precipitation_mm": "Precipitación (mm)"
})
date_range = st.sidebar.date_input("Rango de fechas", [df["date"].min(), df["date"].max()])

# Filtrado
filtered_df = df[(df["city"] == selected_city) &
                (df["date"] >= pd.to_datetime(date_range[0])) &
                (df["date"] <= pd.to_datetime(date_range[1]))]

# Título dinámico
st.subheader(f"{selected_variable.replace('_', ' ').title()} en {selected_city} ({date_range[0]} – {date_range[1]})")

# Gráfico
fig = px.line(filtered_df, x="date", y=selected_variable, title="", labels={
    "date": "Fecha",
    selected_variable: selected_variable.replace("_", " ").title()
})
st.plotly_chart(fig, use_container_width=True)

# Estadísticas
st.markdown("### 📈 Estadísticas")
col1, col2, col3 = st.columns(3)
col1.metric("📉 Mínimo", f"{filtered_df[selected_variable].min():.2f}")
col2.metric("📈 Máximo", f"{filtered_df[selected_variable].max():.2f}")
col3.metric("📊 Promedio", f"{filtered_df[selected_variable].mean():.2f}")