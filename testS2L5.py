import datetime

def assistente_virtuale(comando):
    
    if comando == "1":
        oggi = datetime.date.today()
        risposta = "La data di oggi è " + oggi.strftime("%d/%m/%Y")
        
    elif comando == "2":
        ora_attuale = datetime.datetime.now().time()
        risposta = "L'ora attuale è " + ora_attuale.strftime("%H:%M")
        
    elif comando == "3":
        risposta = "Mi chiamo Assistente Virtuale"
       
    else:
      risposta = "Non ho capito la tua domanda."
    return risposta
    
while True:
    comando_utente = input("Cosa vuoi sapere?\n (1) Qual é la data di oggi?\n (2) Che ore sono?\n (3)Come ti chiami?\n (4)Esci\n Scrivi (1/2/3/4)\n")

    if comando_utente.lower() == "4":
        print("Arrivederci!")
        break
    
    else:
        print(assistente_virtuale(comando_utente)) 