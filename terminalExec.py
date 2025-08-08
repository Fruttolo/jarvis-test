import subprocess

def terminal_exec(command: str) -> str:
    try:
        print("-"*20)
        print(f"COMANDO:\n{command}")
        
        # Esegue il comando e cattura l'output
        risultato = subprocess.run(
            command,
            shell=True,           # Esegue il comando tramite la shell
            capture_output=True,  # Cattura stdout e stderr
            text=True             # Converte output in stringa
        )

        # Stampa output e eventuali errori
        if risultato.stdout:
            print("-"*20)
            print(f"TERMINAL:\n{risultato.stdout}")
            return risultato.stdout
        if risultato.stderr:
            print("-"*20)
            print(f"ERRORE TERMINAL:\n{risultato.stderr}")
            return risultato.stderr

    except Exception as e:
        print("-"*20)
        print(f"ERRORE:\n{e}")
