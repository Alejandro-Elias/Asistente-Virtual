import streamlit as st
from ingresar import ingresar
from registrate import registrate
from chat import chat
import json

st.set_page_config(layout="wide")

if "pantalla" not in st.session_state:
    st.session_state.pantalla = "ingreso"

if "es_usuario" not in st.session_state:
    st.session_state.es_usuario = True

if "esta_logueado" not in st.session_state:
    st.session_state.esta_logueado = False

with open("historia.json", "r") as datos:
    historia_json = json.load(datos)

st.title("Asistente Virtual")

if st.session_state.esta_logueado:
    if st.button("Guardar Chat"):
        with open("historia.json", "w") as datos:

            id = historia_json[-1]["chats"]["id"] + 1 if len(historia_json) > 0 else 1
            nuevo_chat = "chat " + str(id)

            historia_json.append(
            {"user_id": st.session_state.id,
            "chats": {
                "id": id,
                "title": "chat",
                "historia": [st.session_state.chat_history]}
                })       

            json.dump(historia_json, datos)        

chats_usuario = []
nombres_chat = ["-- Selecciona una opción --"] 

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
        st.rerun()
        
    if st.sidebar.button("Nuevo Chat"):
        st.session_state.chat_history = []
        st.session_state.pantalla = "chat"

        
    for i, chat in enumerate(historia_json):

        if chat["user_id"] == st.session_state.id:
            chats_usuario.append(chat["chats"]["historia"])
            nombres_chat.append(chat["chats"]["title"] + str(chat["chats"]["id"]))

    chat_seleccionado = st.sidebar.selectbox("Selecciona un chat", nombres_chat, key="chat_seleccionado")

    #if chat_seleccionado != "-- Selecciona una opción --":
    #    st.session_state.chat_history = chats_usuario

st.sidebar.markdown("---")

mensaje_error = []

if st.session_state.pantalla == "ingreso":
    ingresar()
elif st.session_state.pantalla == "registro":
    registrate()
elif st.session_state.pantalla == "chat":
    chat()
