import streamlit as st
from ingresar import ingresar
from registrate import registrate
from chat import chat
import json
from PIL import Image

imagen = Image.open("sonreir.png")

st.set_page_config(
    page_title="Asistente Virtual",  
    page_icon="sonreir.png",             
    layout="wide",              
    initial_sidebar_state="expanded"  
)

if "pantalla" not in st.session_state:
    st.session_state.pantalla = "ingreso"

if "es_usuario" not in st.session_state:
    st.session_state.es_usuario = True

if "esta_logueado" not in st.session_state:
    st.session_state.esta_logueado = False

if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

if "chat_history_actual" not in st.session_state:
    st.session_state.chat_history_actual = []

historia_json = []
nuevo = False

try:
    with open("historia.json", "r") as datos:
        historia_json = json.load(datos)
except FileNotFoundError:
    print("No se encontro el archivo de historias del chat")
except json.JSONDecodeError:
    print("El archivo no es valido o esta corrupto")
except  Exception as e:
    print(f"Error al leer el archivo de historias del chat: {e.args[0]}")     

col1, col2 = st.columns([11, 1])

with col1:
    subcol1, subcol2 = st.columns([1, 16])

    with subcol1:
        st.image(imagen, width=100)

    with subcol2:
        st.title("Asistente Virtual PYTHON")

chats_usuario = {}
nombres_chat = ["Chat Actual"] 

st.markdown("---")

if st.session_state.esta_logueado:
        
    if st.sidebar.button("Nuevo Chat"):
        st.session_state.chat_history_actual = []
        st.session_state.pantalla = "chat"
        st.rerun()
        nuevo = True

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

    st.sidebar.markdown("---")

    try:        
        for i, chat_historia in enumerate(historia_json):

            if chat_historia["user_id"] == st.session_state.id:
                nombre = chat_historia["chats"]["title"] + str(chat_historia["chats"]["id"])
                nombres_chat.append(nombre)
                chats_usuario[nombre] = chat_historia["chats"]["historia"]

        chat_seleccionado = st.sidebar.selectbox("Selecciona un chat", nombres_chat, key="chat_seleccionado")
        
        if chat_seleccionado != "Chat Actual":
            st.session_state.chat_history = chats_usuario[chat_seleccionado]
            st.session_state.pantalla = "chat"
        else:
            if nuevo:
                st.session_state.chat_history_actual = []
                st.rerun()
            else :
                st.session_state.chat_history = st.session_state.chat_history_actual
    except KeyError:
        print("Una o mas claves son invalidas")
    except Exception as e:
        print(f"Error en el selectbox: {e.args[0]}")
    

else:

    st.sidebar.title("Menú")

    if st.sidebar.button("Ingresar"):
        st.session_state.pantalla = "ingreso"

    if st.sidebar.button("Registrarse"):
        st.session_state.pantalla = "registro"

    st.sidebar.markdown("---")

mensaje_error = []

if st.session_state.pantalla == "ingreso":
    ingresar()
elif st.session_state.pantalla == "registro":
    registrate()
elif st.session_state.pantalla == "chat":
    chat()
