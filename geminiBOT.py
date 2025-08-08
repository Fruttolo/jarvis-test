from terminalExec import terminal_exec
from geminiCall import call_gemini
import json

def exec_gemini_command(com: str):
    user = {
        "terminal": com,
        "user": ""
    }
    user_json = json.dumps(user)
    return call_gemini(user_json)

def ask_gemini(usr: str):
    user = {
        "terminal": "",
        "user": usr
    }
    user_json = json.dumps(user)
    return call_gemini(user_json)

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
        print(res["response"])
    except Exception as e:
        print(f"Errore durante l'esecuzione: {e}")
