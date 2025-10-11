

def comunicacion (pregunta):
    from google import genai
    from dotenv import load_dotenv
    import os  

    load_dotenv()

    api_key = os.getenv("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=pregunta
    )
    return response.text