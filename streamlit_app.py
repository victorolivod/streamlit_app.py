import streamlit as st

st.title('Encuesta de Hábitos y Preferencias')
st.header('Por favor responde las siguientes preguntas:')

with st.form('encuesta_personal'):
    st.subheader('**Tus respuestas**')

    # Pregunta 1
    edad = st.selectbox('¿Cuál es tu rango de edad?', 
                        ['Menos de 18', '18-24', '25-34', '35-44', '45-54', '55 o más'])

    # Pregunta 2
    genero = st.radio('¿Con qué género te identificas?', 
                      ['Femenino', 'Masculino', 'No binario', 'Prefiero no decirlo'])

    # Pregunta 3
    nivel_educativo = st.selectbox('¿Cuál es tu nivel educativo más alto?', 
                                   ['Primaria', 'Secundaria', 'Preparatoria', 'Licenciatura', 'Posgrado'])

    # Pregunta 4
    trabaja_estudia = st.radio('¿Actualmente trabajas o estudias?', 
                               ['Trabajo', 'Estudio', 'Ambos', 'Ninguno'])

    # Pregunta 5
    horas_dormir = st.slider('¿Cuántas horas duermes en promedio por noche?', 0, 12, 7)

    # Pregunta 6
    deporte = st.radio('¿Realizas actividad física regularmente?', 
                       ['Sí', 'No'])

    # Pregunta 7
    comida_fav = st.selectbox('¿Cuál es tu tipo de comida favorita?', 
                              ['Mexicana', 'Italiana', 'Japonesa', 'China', 'Vegetariana', 'Otra'])

    # Pregunta 8
    redes_sociales = st.multiselect('¿Qué redes sociales usas con frecuencia?', 
                                    ['Facebook', 'Instagram', 'TikTok', 'X (Twitter)', 'LinkedIn', 'Ninguna'])

    # Pregunta 9
    mascotas = st.checkbox('¿Tienes mascotas?')

    # Pregunta 10
    satisfaccion = st.select_slider('¿Qué tan satisfecho/a estás con tu vida actualmente?', 
                                    options=['Muy insatisfecho/a', 'Insatisfecho/a', 'Neutral', 'Satisfecho/a', 'Muy satisfecho/a'])

    # Botón para enviar
    enviado = st.form_submit_button('Enviar')

# Mostrar resultados si se envió
if enviado:
    st.markdown(f'''
    ### ✅ ¡Gracias por participar!
    **Tus respuestas:**
    - Edad: `{edad}`
    - Género: `{genero}`
    - Nivel educativo: `{nivel_educativo}`
    - Actividad principal: `{trabaja_estudia}`
    - Horas de sueño: `{horas_dormir}`
    - Realiza ejercicio: `{deporte}`
    - Comida favorita: `{comida_fav}`
    - Redes sociales: `{', '.join(redes_sociales) if redes_sociales else 'Ninguna'}`
    - ¿Tiene mascotas?: `{'Sí' if mascotas else 'No'}`
    - Satisfacción con la vida: `{satisfaccion}`
    ''')
else:
    st.info('☝️ Responde la encuesta y presiona "Enviar"')
