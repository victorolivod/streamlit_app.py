import streamlit as st

st.header('Selecciona tus preferencias')

actividades = st.multiselect(
    '¿Qué actividades disfrutas en tu tiempo libre?',
    ['Leer', 'Escuchar música', 'Salir con amigos', 'Ver series', 'Hacer ejercicio'],
    default=['Escuchar música', 'Ver series']
)
st.write('Actividades seleccionadas:', actividades)

comidas = st.multiselect(
    '¿Qué comidas te encantan y nunca rechazarías?',
    ['Pizza', 'Tacos', 'Hamburguesas', 'Sushi', 'Pasta'],
    default=['Pizza', 'Tacos']
)
st.write('Tus favoritas:', comidas)

viajes = st.multiselect(
    '¿A qué lugares te gustaría viajar?',
    ['Japón', 'Italia', 'Islandia', 'Perú', 'Canadá'],
    default=['Japón', 'Italia']
)
st.write('Te gustaría ir a:', viajes)

apps = st.multiselect(
    '¿Qué apps usas casi todos los días?',
    ['WhatsApp', 'Instagram', 'Spotify', 'YouTube', 'Google Maps'],
    default=['WhatsApp', 'YouTube']
)
st.write('Usas frecuentemente:', apps)

habitos = st.multiselect(
    '¿Qué hábitos intentas mantener con regularidad?',
    ['Dormir bien', 'Comer saludable', 'Estudiar', 'Hacer ejercicio', 'Leer'],
    default=['Dormir bien', 'Comer saludable']
)
st.write('Tus hábitos seleccionados:', habitos)
