import os
import google.generativeai as genai
from dotenv import load_dotenv
import json

# Carica le variabili d'ambiente dal file .env
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model_name = os.getenv("GEMINI_MODEL")


with open("jarvis_prompt.txt", "r", encoding="utf-8") as f:
    contesto = f.read()

model = genai.GenerativeModel(model_name, system_instruction=contesto)

chat = model.start_chat()

def reset_chat():
    global chat
    chat = model.start_chat()

def call_gemini(prompt: str) -> str:

    try:
        response = chat.send_message(
            prompt,
            safety_settings={
                'HARASSMENT': 'BLOCK_NONE',
                'HATE': 'BLOCK_NONE',
                'SEXUALLY_EXPLICIT': 'BLOCK_NONE',
                'DANGEROUS': 'BLOCK_NONE'
            }
        )
        
        res = response.text.replace("```json", "").replace("```", "").strip()
        response = json.loads(res)
        return response
    
    except Exception as e:
        return f"Si è verificato un errore: {e}"

