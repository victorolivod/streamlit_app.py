import streamlit as st

st.header('preferencias personales')

# Pregunta 1: ¿Cuál es tu forma favorita de pasar un domingo?
domingo = st.selectbox(
    '¿Cómo prefieres pasar un domingo?',
    ('Dormir hasta tarde', 'Salir con amigos', 'Ver series o películas', 'Hacer algo productivo')
)
st.write('Tu plan de domingo es:', domingo)

# Pregunta 2: ¿Qué música sueles escuchar más?
musica = st.selectbox(
    '¿Qué tipo de música escuchas más seguido?',
    ('Rock', 'Reguetón', 'Pop', 'Instrumental / Lo-fi')
)
st.write('Tu estilo de música es:', musica)

# Pregunta 3: ¿Qué bebida prefieres para concentrarte?
bebida = st.selectbox(
    'Cuando estudias o trabajas, ¿qué sueles tomar?',
    ('Café', 'Té', 'Agua', 'Nada')
)
st.write('Prefieres tomar:', bebida)

# Pregunta 4: ¿A qué hora te concentras mejor?
concentracion = st.selectbox(
    '¿Cuál es tu mejor momento del día para concentrarte?',
    ('Mañana temprano', 'Tarde', 'Noche', 'Depende del día')
)
st.write('Tu mejor momento es:', concentracion)

# Pregunta 5: ¿Qué tipo de películas prefieres?
peliculas = st.selectbox(
    '¿Qué tipo de películas te gustan más?',
    ('Suspenso', 'Comedia', 'Ciencia ficción', 'Drama')
)
st.write('Tu tipo favorito de películas es:', peliculas)

