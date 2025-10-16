

def comunicacion (pregunta):
    from google import genai
    from dotenv import load_dotenv
    import os  

    load_dotenv()

    try:
        api_key = os.getenv("GEMINI_API_KEY")

        client = genai.Client(api_key=api_key)

        response = client.models.generate_content(
            model="gemini-2.5-flash", contents=pregunta
        )
    except ValueError as e:
        print(f"⚠️ Error en configuración: {e}")

    except genai.types.generation_types.GenerationError as e:
        print(f"❌ Error al generar contenido: {e}")

    except ConnectionError:
        print("🌐 Error de conexión al intentar acceder al servicio de Gemini.")

    except Exception as e:
        print(f"😬 Ocurrió un error inesperado: {e.args[0]}")

    
    return response.text