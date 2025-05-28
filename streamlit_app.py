import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write con datos clínicos simulados')

st.write('Mostrando información de pacientes del estudio clínico 2025.')

st.write(42)  # Por ejemplo, número de pacientes en observación

pacientes_df = pd.DataFrame({
    'ID Paciente': [2001, 2002, 2003, 2004],
    'Edad': [34, 58, 45, 29],
    'Presión Sistólica': [120, 145, 132, 118]
})
st.write(pacientes_df)

st.write('Datos vitales registrados:', pacientes_df, 'Fin de la muestra.')

datos_vitales = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['Frecuencia Cardíaca', 'Temperatura', 'Nivel de Oxígeno']
)
grafico = alt.Chart(datos_vitales).mark_circle().encode(
    x='Frecuencia Cardíaca',
    y='Temperatura',
    size='Nivel de Oxígeno',
    color='Nivel de Oxígeno',
    tooltip=['Frecuencia Cardíaca', 'Temperatura', 'Nivel de Oxígeno']
)
st.write(grafico)
