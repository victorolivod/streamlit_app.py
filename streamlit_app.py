import streamlit as st

st.header('¿Qué soluciones de análisis te interesan más?')

st.write('Selecciona los servicios que te interesan para tu empresa o proyecto:')

# Opciones tipo checkbox con otro enfoque
analisis_clientes = st.checkbox('Segmentación de clientes')
analisis_ventas = st.checkbox('Análisis de tendencias de ventas')
alertas = st.checkbox('Alertas automáticas por umbrales')
panel_ejecutivo = st.checkbox('Panel de control para gerencia')
integracion_datos = st.checkbox('Integración de datos desde distintas fuentes')
#RESPUESTAS
if analisis_clientes:
    st.write('🔍 Anotado: análisis para entender mejor a tus clientes.')
if analisis_ventas:
    st.write('📈 Consideraremos herramientas para detectar tendencias y cambios en ventas.')
if alertas:
    st.write('🚨 Agendamos tu interés en configurar alertas automáticas por condiciones específicas.')
if panel_ejecutivo:
    st.write('📊 Te mostraremos un panel con indicadores clave para la alta dirección.')
if integracion_datos:
    st.write('🔗 Registrado: integración de múltiples fuentes de datos en un solo flujo.')
