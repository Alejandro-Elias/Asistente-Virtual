import streamlit as st
import json
from chat import chat

def ingresar():

    usuarios_json = []

    try:
        with open("usuarios.json", "r") as datos:
            usuarios_json = json.load(datos)
    except FileNotFoundError:
        print("No se encontro el archivo de historias del chat")
    except json.JSONDecodeError:
        print("El archivo no es valido o esta corrupto")
    except  Exception as e:
        print(f"Error al leer el archivo de historias del chat: {e.args[0]}")    

    if "id" not in st.session_state:
        st.session_state.id = 0

    if "mensaje_error" not in st.session_state:
        st.session_state.mensaje_error = []

    if st.session_state.pantalla == "chat":
        chat()
    else:     
        st.subheader("Ingresar")
        
        col1, col2, col3, col4 = st.columns([4, 2, 3, 3])
        with col1:
            with st.form("login_form"):
                email = st.text_input("Ingrese su email", key="email_ingreso")
                contrasenia = st.text_input("Ingrese su contraseña", type="password", key="contrasenia")
                submit_button = st.form_submit_button("Ingresar")

            if submit_button:

                sub_col1, sub_col2, sub_col3 = st.columns([6, 1.5, 4])


                with sub_col3:
                

                    if not email:
                        st.session_state.mensaje_error.append("El email es requerido")
                    if not contrasenia:
                        st.session_state.mensaje_error.append("La contraseña es requerida")

                    contador_email = 0
                    contador_contrasenia = 0
                    for user in usuarios_json:
                        if user["email"].lower().strip() == email.lower().strip():
                            contador_email += 1
                        if user["contrasenia"] == contrasenia:
                            contador_contrasenia += 1
                        if user["email"].lower().strip() == email.lower().strip() and user["contrasenia"] == contrasenia:
                            st.session_state.id = user["id"]


                    if contador_email == 0:
                        st.session_state.mensaje_error.append("El email es incorrecto")

                    if contador_contrasenia == 0:
                            st.session_state.mensaje_error.append("La contraseña es incorrecta")
                    with col3:
                        if len(st.session_state.mensaje_error) > 0:
                            for error in st.session_state.mensaje_error:
                                st.write(error)
                                st.session_state.mensaje_error = []

                    if contador_email > 0 and contador_contrasenia > 0:
                        st.session_state.esta_logueado = True
                        st.session_state.pantalla = "chat"
                        st.success("Bienvenido") 
                        st.rerun()

