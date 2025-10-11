import streamlit as st
import json
from comunicacionIA import comunicacion


def chat():

    usuarios_json = []

    try:
        with open("usuarios.json", "r") as datos:
            usuarios_json = json.load(datos)
    except FileNotFoundError:
        print("No se encontro el archivo de usuarios")
    except json.JSONDecodeError:
        print("El archivo no es valido o esta corrupto")
    except  Exception as e:
        print(f"Error al leer el archivo de usuarios: {e.args[0]}")    

    if "id" not in st.session_state:
        st.session_state.id = 0
    nombre = ""

    for user in usuarios_json:
        if user["id"] == st.session_state.id:
            nombre = user["nombre"]

    col1, col2, col3 = st.columns([5, 90, 5])
    with col2:
        with st.chat_message("assistant"):
            st.write(f"Hola {nombre}, soy tu asistente virtual. En que puedo ayudarte?")

    consulta = st.chat_input("Ingresa tu pregunta")

    if consulta:
        respuesta = comunicacion(consulta)

        st.session_state.chat_history_actual.append({
            "consulta" : consulta,
            "respuesta" : respuesta
        })

    for chat in st.session_state.chat_history:
            

        col1, col2, col3 = st.columns([40, 55, 5])

        with col2:
            with st.chat_message("user"):
                st.write(chat["consulta"])

        col1, col2, col3 = st.columns([5, 90, 5])

        with col2:
            with st.chat_message("assistant"):
                st.write(chat["respuesta"])