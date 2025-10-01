import streamlit as st
from ingresar import ingresar
from registrate import registrate
from chat import chat

st.set_page_config(layout="wide")

if "pantalla" not in st.session_state:
    st.session_state.pantalla = "ingreso"

if "es_usuario" not in st.session_state:
    st.session_state.es_usuario = True

if "esta_logueado" not in st.session_state:
    st.session_state.esta_logueado = False

st.title("Asistente Virtual")

st.markdown("---")

st.sidebar.title("Menú")

if st.sidebar.button("Ingresar"):
    st.session_state.pantalla = "ingreso"

if st.sidebar.button("Registrarse"):
    st.session_state.pantalla = "registro"


if st.session_state.esta_logueado:


    if st.sidebar.button("Salir"):
        st.session_state.clear()
        st.session_state.pantalla = "ingreso"
        st.session_state.mensaje_error = []
        st.session_state.chat_history = []
        st.session_state.esta_logueado = False
        st.session_state.id = 0
        st.session_state.email_ingreso = ""
        st.session_state.contrasenia = ""
        
    if st.sidebar.button("Nuevo Chat"):
        st.session_state.chat_history = []
        st.session_state.pantalla = "chat"

mensaje_error = []

if st.session_state.pantalla == "ingreso":
    ingresar()
elif st.session_state.pantalla == "registro":
    registrate()
elif st.session_state.pantalla == "chat":
    chat()