
import openai
import os
from dotenv import load_dotenv
load_dotenv()

def call_chatgpt(prompt: str, model: str = "gpt-3.5-turbo") -> str:
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()