import streamlit as st
import json


def chat():
    with open("usuarios.json", "r") as datos:
        usuarios_json = json.load(datos)

    if "id" not in st.session_state:
        st.session_state.id = 0

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    with open("historia.json", "r") as datos:
        historia_json = json.load(datos)

    nombre = ""

    id = historia_json[-1]["id"] + 1 if len(historia_json) > 0 else 1
    nuevo_chat = "chat " + str(id)

    historia_json.append({
            "id": id,
            "title": nuevo_chat,
            "historia": []}
            )

    for user in usuarios_json:
        if user["id"] == st.session_state.id:
            nombre = user["nombre"]

    col1, col2, col3 = st.columns([5, 90, 5])
    with col2:
        with st.chat_message("assistant"):
            st.write(f"Hola {nombre}, soy tu asistente virtual. En que puedo ayudarte?")

    consulta = st.chat_input("Ingresa tu pregunta")
    respuesta = "Estoy procesando tu pregunta..."

    if consulta:

        st.session_state.chat_history.append({
            "consulta" : consulta,
            "respuesta" : respuesta
        })

        historia_json[-1]["historia"].append({
            "consulta" : consulta,
            "respuesta" : respuesta
        })

        with open("historia.json", "w") as datos:
            json.dump(historia_json, datos)

        for chat in st.session_state.chat_history:
            

            col1, col2, col3 = st.columns([40, 55, 5])

            with col2:
                with st.chat_message("user"):
                    st.write(chat["consulta"])

            col1, col2, col3 = st.columns([5, 90, 5])

            with col2:
                with st.chat_message("assistant"):
                    st.write(chat["respuesta"])