import streamlit as st
from datetime import time, datetime

st.header('Mi propia versión utilizando diferentes datos')

st.subheader('Slider')
horas_sueño = st.slider('¿Cuántas horas duermes normalmente por noche?', 0, 12, 7)
st.write("Duermes", horas_sueño, "horas por noche")

st.subheader('Range slider')
frecuencia = st.slider(
    'Selecciona tu rango de frecuencia cardíaca en reposo (lpm)',
    40.0, 100.0, (60.0, 80.0)
)
st.write('Rango seleccionado:', frecuencia)

st.subheader('Range time slider')
horario_tutorias = st.slider(
    "Selecciona tu horario disponible para tutorías:",
    value=(time(14, 0), time(16, 30))
)
st.write("Tu horario disponible es:", horario_tutorias)

st.subheader('Datetime slider')
proximo_examen = st.slider(
    "¿Cuándo es tu próximo examen?",
    value=datetime(2025, 6, 10, 8, 0),
    format="MM/DD/YY - hh:mm"
)
st.write("Tu examen será el:", proximo_examen)
