#Realizzare un programma Python per collezionare i film visti. Memorizzare  il nome del film, l'anno di uscita e la cifra di incassi al botteghino. 
#Fare in modo che si possa inserire, modificare, visualizzare e cancellare un film. Il programma deve anche salvare i film su file e ricaricarli all'avvio.
 
#Provare a fare due funzioni salva e due funzioni carica. Una coppia carica/salva usa la strategia con separatore; una coppia carica/salva usa la strategia basata su json.
 

NOME_FILE= "film.txt"

def stampaMenu():
    print("Scegli:")
    print("1 - per inserire un nuovo film")
    print("2 - per visualizzare tutti i film che hai visto")
    print("3 - modifica film")
    print("4 - eliminare un film")
    print("0 - terminare il programma")
 
 
def Salva_Separatore(dizionario):
   
    file = open(f"./{NOME_FILE}","w")
    for k in dizionario:
        v = dizionario[k]
        file.write(f"{k};{v[0]};{v[1]}\n")
    file.close()
 
def Carica_Separatore():

    import os
    try:
        
            file = open(f"./{NOME_FILE}","r")
            dizionario = {}
            for riga in file:
                riga = riga.strip()
                campi = riga.split(";")
                nome = campi[0]
                anno = campi[1]
                incassi = campi[2]
                dizionario[nome] = (anno,incassi)
            file.close()
            return dizionario
    except:
        print("Impossibile caricare il file")
        return {}
        
def Salva_JSON(dizionario):
    import json
    file = open(f"./{NOME_FILE}","w")
    json.dump(dizionario,file)
    file.close()

def Scelta():
    corretto = False
    while not corretto:
        try:
            scelta = input("Scelta >> ")
            if int(scelta) < 0 or int(scelta) > 3:
                print("Scelta non valida")
                corretto = False
            else:
                corretto = True
                return scelta
        except:
            print("Formato scelta non valida")
            corretto = False
 
def InserisciNomeFilm():
    corretto = False
    while not corretto:
        nome = input("Nome del film >> ")
        if len(nome) == 0:
            print("Il nome del film non può essere vuoto")
            corretto = False
        else:
            corretto = True
            return nome

def InserisciAnnoFilm():
    from datetime import datetime
    errore=True
    while errore:
            data = input("Data di uscita (gg/mm/aaaa) >> ")
           
            try:
               
                data_nascita = datetime.strptime(data, "%d/%m/%Y")
                if data_nascita > datetime.now():
                    print("Data non valida, riprovare")
                else:
                    errore=False                
                    return data_nascita
           
            except:
                print("Data non valida, riprovare")

def InserisciIncassiFilm():
    corretto = False
    while not corretto:
        try:
            incassi = float(input("Incassi al botteghino >> "))
            if incassi < 0:
                print("Incassi non validi")
                corretto = False
            else:
                corretto = True
                return incassi
        except:
            print("Formato incassi non valido")
            corretto = False

def VisualizzaFilm(dizionario):

    if len(dizionario) == 0:
        print("Non hai ancora inserito nessun film")
    else:
        for k in dizionario:
            v = dizionario[k]
            print(f"{k} - {v[0]} - {v[1]}")

def ModificaFilm(dizionario):

    if len(dizionario) == 0:
        print("Non hai ancora inserito nessun film")
    else:
        nome = input("Nome del film da modificare >> ")
        if nome in dizionario:
            anno = InserisciAnnoFilm()
            incassi = InserisciIncassiFilm()
            dizionario[nome] = (anno,incassi)
            print("Film modificato correttamente")
        else:
            print("Film non trovato")

def EliminaFilm(dizionario):

    if len(dizionario) == 0:
        print("Non hai ancora inserito nessun film")
    else:
        nome = input("Nome del film da eliminare >> ")
        if nome in dizionario:
            del dizionario[nome]
            print("Film eliminato correttamente")
        else:
            print("Film non trovato")


film_visti = Carica_Separatore()
scelta = ""
while scelta != 0:
    stampaMenu()
    scelta = Scelta()
    if scelta == "1":
        nome = InserisciNomeFilm()
        anno = InserisciAnnoFilm()
        incassi = InserisciIncassiFilm()
        film_visti[nome] = (anno,incassi)


    elif scelta == "2":
        VisualizzaFilm(film_visti)
    elif scelta == "3":
        ModificaFilm(film_visti)
    elif scelta == "4":
        EliminaFilm(film_visti)
    elif scelta == "0":
        print("Arrivederci!")
        Salva_Separatore(film_visti)


