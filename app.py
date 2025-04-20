import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv(
    "C:/Users/carre/OneDrive/Documentos/Data_Analyst/Control_Panel_Project/CPL_/vehicles_us.csv")

st.header('Análisis de Vehículos en Venta (USA)')

# Botón para histograma
if st.button('Construir histograma'):
    st.write('Histograma de la columna odómetro')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Botón para scatter
if st.button('Construir gráfico de dispersión'):
    st.write('Gráfico de precio vs año del modelo')
    fig = px.scatter(car_data, x="model_year", y="price")
    st.plotly_chart(fig, use_container_width=True)
