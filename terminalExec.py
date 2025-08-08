import subprocess

def terminal_exec(command: str) -> str:
    try:
        print(f"COMANDO:\n{command}")
        input()
        
        # Esegue il comando e cattura l'output
        risultato = subprocess.run(
            command,
            shell=True,           # Esegue il comando tramite la shell
            capture_output=True,  # Cattura stdout e stderr
            text=True             # Converte output in stringa
        )

        # Stampa output e eventuali errori
        if risultato.stdout:
            return risultato.stdout
        if risultato.stderr:
            return risultato.stderr

    except Exception as e:
        print(f"Errore durante l'esecuzione: {e}")
