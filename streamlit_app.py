import streamlit as st
import time

st.set_page_config(layout="wide")
st.title('Demostración de múltiples barras de progreso')

with st.expander('¿Cómo funciona esto?'):
    st.write("""
        Este ejemplo muestra cómo manejar varias barras de progreso que avanzan a diferentes ritmos.
        Es útil para simular tareas con distintos tiempos de ejecución.
    """)

# Colocamos las 3 barras en columnas para visualizarlas en paralelo
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Carga rápida")
    progress1 = st.progress(0)
    for i in range(100):
        time.sleep(0.01)  # Muy rápida
        progress1.progress(i + 1)

with col2:
    st.subheader("Carga media")
    progress2 = st.progress(0)
    for i in range(100):
        time.sleep(0.03)  # Velocidad intermedia
        progress2.progress(i + 1)

with col3:
    st.subheader("Carga lenta")
    progress3 = st.progress(0)
    for i in range(100):
        time.sleep(0.06)  # Más lenta
        progress3.progress(i + 1)

st.success("Las tres cargas han finalizado correctamente.")

