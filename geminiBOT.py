from terminalExec import terminal_exec
from geminiCall import GeminiChatManager
import json

chat_manager = GeminiChatManager()

def exec_gemini_command(com: str):
    user = {
        "terminal": com,
        "user": ""
    }
    user_json = json.dumps(user)
    return chat_manager.call_gemini(user_json)

def ask_gemini(usr: str):
    user = {
        "terminal": "",
        "user": usr
    }
    user_json = json.dumps(user)
    return chat_manager.call_gemini(user_json)

def reset_chat():
    chat_manager.start_new_chat()

def geminiBOT(req: str):
    res = ask_gemini(req)
    try:
        if(res["error"] != ""):
                raise Exception(res["error"])
        while res["commands"] != "":
            terminalOutPut = terminal_exec(res["commands"])
            res = exec_gemini_command(terminalOutPut)
            if(res["error"] != ""):
                raise Exception(res["error"])
        print("-"*20)
        print(f"RISPOSTA:\n{res['response']}")
        return res["response"]
    except Exception as e:
        print("-"*20)
        print(f"ERRORE:\n{e}")
        return f"Errore durante l'esecuzione: {e}"
