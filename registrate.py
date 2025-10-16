import streamlit as st
import json

def registrate():

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

    if "nombre" not in st.session_state:
        st.session_state.nombre = ""

    if "email" not in st.session_state:
        st.session_state.email = ""

    if "contrasenia" not in st.session_state:    
        st.session_state.contrasenia = ""

    usuario = {
        "id": usuarios_json[-1]["id"] + 1 if len(usuarios_json) > 0 else 1,
        "nombre": "",
        "email": "",
        "contrasenia": ""
    }

    col1, col2, col3 = st.columns(3)
    with col2:

        st.subheader("Registrate")
        with st.form("registro_form"):
            usuario["nombre"] = st.text_input("Ingrese su nombre", key="nombre")
            usuario["email"] = st.text_input("Ingrese su Email", key="Email")
            usuario["contrasenia"] = st.text_input("Ingrese su contraseña", type="password", key="contrasenia")
            submit_button = st.form_submit_button("Registrarme")

    if submit_button:

        sub_col1, sub_col2 = st.columns([6, 4.5])
        with sub_col2:    
            usuarios_json.append(usuario)
            try:
                with open("usuarios.json", "w") as datos:
                    json.dump(usuarios_json, datos)
                    st.success("Usuario guardado con exito")
            except:
                print(f"Error al guardar el usuario: {e.args[0]}")

            st.session_state.esta_logueado = True
            st.session_state.id = usuario["id"]
            st.session_state.pantalla = "chat"
            st.rerun()
