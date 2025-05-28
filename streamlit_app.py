import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.set_page_config(layout="wide")
st.title('Panel Interactivo - Danu Analítica')

# Sección 1: Explicación
with st.expander('Acerca de esta aplicación'):
    st.write("""
        Esta aplicación muestra cómo estructurar un panel en varias secciones usando Streamlit.
        Se incluyen gráficos, controles de entrada y visualización de datos.
    """)
    st.image('https://upload.wikimedia.org/wikipedia/commons/3/38/Streamlit_logo_mark.png', width=200)

# Sidebar: Datos del usuario
st.sidebar.header('Información del usuario')
nombre = st.sidebar.text_input('Nombre completo:')
departamento = st.sidebar.selectbox('Área de trabajo:', ['-- Seleccionar --', 'Ventas', 'Marketing', 'Finanzas', 'Operaciones'])
experiencia = st.sidebar.slider('Nivel de experiencia (1 a 10):', 1, 10, 5)

# Sección 2: Mensaje personalizado
st.header('Sección 1: Bienvenida')
if nombre and departamento != '-- Seleccionar --':
    st.write(f'Bienvenido/a {nombre}. Has seleccionado el área de {departamento}.')
else:
    st.write('Por favor, completa tus datos en la barra lateral.')

# Sección 3: Botón
st.header('Sección 2: Interacción simple')
if st.button('Haz clic aquí'):
    st.write('Gracias por interactuar. Sigue explorando el panel.')

# Sección 4: Gráfico de líneas
st.header('Sección 3: Visualización de datos (línea)')
df_linea = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['Producto A', 'Producto B', 'Producto C']
)
st.line_chart(df_linea)

# Sección 5: Gráfico de dispersión
st.header('Sección 4: Gráfico de dispersión')
df_disp = pd.DataFrame(
    np.random.randn(100, 3),
    columns=['x', 'y', 'tamaño']
)
chart = alt.Chart(df_disp).mark_circle().encode(
    x='x',
    y='y',
    size='tamaño',
    color='tamaño',
    tooltip=['x', 'y', 'tamaño']
)
st.altair_chart(chart, use_container_width=True)

# Sección 6: Carga de datos
st.header('Sección 5: Subida de archivo')
archivo = st.file_uploader("Sube un archivo CSV para visualizar sus datos:")
if archivo is not None:
    df_archivo = pd.read_csv(archivo)
    st.subheader("Vista previa del archivo cargado")
    st.write(df_archivo.head())
    st.subheader("Estadísticas básicas")
    st.write(df_archivo.describe())
else:
    st.write("Aún no se ha subido ningún archivo.")

