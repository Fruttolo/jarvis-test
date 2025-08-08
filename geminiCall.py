
import os
import google.generativeai as genai
from dotenv import load_dotenv
import json

class GeminiChatManager:
    def __init__(self):
        # Carica le variabili d'ambiente dal file .env
        load_dotenv()
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        model_name = os.getenv("GEMINI_MODEL")
        with open("jarvis_prompt.txt", "r", encoding="utf-8") as f:
            contesto = f.read()
        self.model = genai.GenerativeModel(model_name, system_instruction=contesto)
        self.chat = self.model.start_chat()
        self.chatId = 1
        print("-"*20)
        print(f"STARTED CHAT: {self.chatId}")

    def start_new_chat(self):
        self.chat = self.model.start_chat()
        self.chatId += 1
        print("-"*20)
        print(f"NEW CHAT SESSION: {self.chatId}")

    def call_gemini(self, prompt: str) -> str:
        try:
            response = self.chat.send_message(
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