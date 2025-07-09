import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar datos
def load_data():
    df = pd.read_csv("nasa_clima_espana_1984_hoy.csv", parse_dates=["Fecha"])
    return df

df = load_data()

st.title("🌍 Dashboard Climático de Ciudades Españolas")
st.markdown("Datos diarios desde **1984 hasta hoy** para temperatura, humedad y precipitaciones. Fuente: [NASA POWER](https://power.larc.nasa.gov/)")

# Cambio nombres de las colunmas


# Sidebar
st.sidebar.header("Opciones")
selected_city = st.sidebar.selectbox("Selecciona una ciudad", sorted(df["Ciudad"].unique()))
selected_variable = st.sidebar.selectbox("Variable a visualizar", {
    "Temperatura (°C)",
    "Humedad relativa (%)",
    "Precipitación (mm)"
    })
date_range = st.sidebar.date_input("Rango de fechas", [df["Fecha"].min(), df["Fecha"].max()])

# Filtrado
filtered_df = df[(df["Ciudad"] == selected_city) &
                (df["Fecha"] >= pd.to_datetime(date_range[0])) &
                (df["Fecha"] <= pd.to_datetime(date_range[1]))]

# Título dinámico
st.subheader(f"{selected_variable.replace('_', ' ').title()} en {selected_city} ({date_range[0]} – {date_range[1]})")

# Gráfico
fig = px.line(filtered_df, x="Fecha", y=selected_variable, title="", labels={
    "Fecha": "Fecha",
    selected_variable: selected_variable.replace("_", " ").title()
})
st.plotly_chart(fig, use_container_width=True)

# Estadísticas
st.markdown("### 📈 Estadísticas")
col1, col2, col3 = st.columns(3)
col1.metric("📉 Mínimo", f"{filtered_df[selected_variable].min():.2f}")
col2.metric("📈 Máximo", f"{filtered_df[selected_variable].max():.2f}")
col3.metric("📊 Promedio", f"{filtered_df[selected_variable].mean():.2f}")