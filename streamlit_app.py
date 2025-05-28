import streamlit as st
st.header('Interacción con botones')
if st.button('Saludar'):
    st.write('¡Hola! Qué bueno verte por aquí.')
if st.button('Inspirarme'):
    st.write('Recuerda: cada paso pequeño te acerca a algo grande.')
if st.button('Dime algo curioso'):
    st.write('¿Sabías que el corazón de un camarón está en su cabeza?')
