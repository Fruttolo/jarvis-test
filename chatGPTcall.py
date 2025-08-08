
import openai
import os
from dotenv import load_dotenv
load_dotenv()

def call_chatgpt(prompt: str) -> str:
    openai.api_key = os.getenv("OPENAI_API_KEY")
    model = os.getenv("OPENAI_MODEL")
    response = openai.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()