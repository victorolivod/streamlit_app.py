import streamlit as st
import pandas as pd
import numpy as np

# Encabezado general de la app
st.header('Visualización de datos con charts')

st.subheader('Gráfico de línea: Temperatura promedio')
temperaturas = pd.DataFrame(
    np.random.randint(15, 35, size=(10, 3)),
    columns=['Ciudad A', 'Ciudad B', 'Ciudad C']
)
st.line_chart(temperaturas)

st.subheader('Gráfico de área: Producción mensual')
produccion = pd.DataFrame({
    'Enero': [120, 100, 90],
    'Febrero': [130, 105, 95],
    'Marzo': [140, 110, 100]
}, index=['Línea 1', 'Línea 2', 'Línea 3']).T
st.area_chart(produccion)

st.subheader('Gráfico de barras: Estudiantes por carrera')
estudiantes = pd.DataFrame({
    'Ingeniería': [200],
    'Medicina': [180],
    'Arquitectura': [120],
    'Derecho': [160]
})
st.bar_chart(estudiantes.T)

