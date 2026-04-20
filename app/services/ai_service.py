import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def analyze_text_with_gemini(text):
    # Usamos EXACTAMENTE uno de los nombres que salieron en tu terminal
    model_name = 'models/gemini-2.0-flash-lite-001'
    
    try:
        model = genai.GenerativeModel(model_name)
        prompt = f"Resume este texto en 3 puntos clave:\n\n{text[:3000]}"
        
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error con el modelo {model_name}: {str(e)}"
