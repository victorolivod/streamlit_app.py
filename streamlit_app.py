import streamlit as st
import pandas as pd

st.title('Cargador de archivos - Danu Analítica')

# Primer archivo: Datos de ventas
st.subheader('🔽 Cargar archivo de ventas (CSV)')
ventas_file = st.file_uploader("Selecciona el archivo de ventas", key="ventas")

if ventas_file is not None:
    ventas_df = pd.read_csv(ventas_file)
    st.subheader('📊 Datos de Ventas')
    st.write(ventas_df)
    st.subheader('📈 Estadísticas descriptivas - Ventas')
    st.write(ventas_df.describe())
else:
    st.info('☝️ Carga un archivo CSV con los datos de ventas.')

st.markdown("---")

# Segundo archivo: Datos de clientes
st.subheader('🔽 Cargar archivo de clientes (CSV)')
clientes_file = st.file_uploader("Selecciona el archivo de clientes", key="clientes")

if clientes_file is not None:
    clientes_df = pd.read_csv(clientes_file)
    st.subheader('📊 Datos de Clientes')
    st.write(clientes_df)
    st.subheader('📈 Estadísticas descriptivas - Clientes')
    st.write(clientes_df.describe())
else:
    st.info('☝️ Carga un archivo CSV con los datos de clientes.')
