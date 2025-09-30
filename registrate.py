import streamlit as st
import json

def registrate():

    with open("usuarios.json", "r") as datos:
        usuarios_json = json.load(datos)

    if "nombre" not in st.session_state:
        st.session_state.nombre = ""

    if "email" not in st.session_state:
        st.session_state.email = ""

    if "contrasenia" not in st.session_state:    
        st.session_state.contrasenia = ""

    usuario = {
        "id": usuarios_json[len(usuarios_json) - 1]["id"] + 1,
        "nombre": "",
        "email": "",
        "contrasenia": ""
    }

    st.subheader("Registrate")

    col1, col2, col3 = st.columns(3)
    with col1:
        usuario["nombre"] = st.text_input("Ingrese su nombre", key="nombre")
        usuario["email"] = st.text_input("Ingrese su Email", key="Email")
        usuario["contrasenia"] = st.text_input("Ingrese su contraseña", type="password", key="contrasenia")

        sub_col1, sub_col2 = st.columns([6, 4.5])
        with sub_col2:    
            if st.button("registrarme", key="btn_registrar"):
                st.session_state.esta_logueado = True
                usuarios_json.append(usuario)
                with open("usuarios.json", "w") as datos:
                    json.dump(usuarios_json, datos)
