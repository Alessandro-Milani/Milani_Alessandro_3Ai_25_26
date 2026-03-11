import os
print(os.getcwd())
NOME_FILE= "film.txt"

def stampaMenu():
    print("Scegli:")
    print("1 - per inserire un nuovo film")
    print("2 - per visualizzare tutti i film che hai visto")
    print("3 - eliminare un film")
    print("0 - terminare il programma")
 
 
def Salva(lista):
   
    file = open(f"./{NOME_FILE}","w")
    for f in lista:
        file.write(f"{f}\n")
    file.close()
 
def Carica(): 
       
    try:
        
        file = open(f"{NOME_FILE}","r")
       
        risultato=[]

        s=file.readline()[:-1]
        while s!="":
            risultato.append(s)
            s=file.readline()[:-1]

        file.close() 
        return risultato

    except:
        print("Impossibile caricare il file")
        return []
 

def scelta():
    corretto = False
    while not corretto:
        try:
            scelta = int(input("Scelta >> "))
            if scelta < 0 or scelta > 3:
                print("Scelta non valida")
                corretto = False
            else:
                corretto = True  
                return scelta          
        except:
            print("Formato scelta non valida")
            corretto = False
 
 
def chiediFilm(cortometraggi):
    corretto = False
    while not corretto:
        nome = input("Inserisci il nome del film ").strip().lower()
        if len(nome) == 0:
            print("Nome film non valido")
        if nome in cortometraggi:
            print("Film già presente in archivio")        
        else:
            corretto = True
            return nome
 
def inserisciFilm(f):
    nome = chiediFilm(f)
    f.append(nome)
 
def eliminaFilm(f):
    visualizzaFilm(f)
    posizione = chiediPosizione(f)
    f.pop(posizione-1)
 
def chiediPosizione(f):
    corretto = False
    while not corretto:
        try:
            scelta = int(input("Indica il numero del film da modificare "))
            if scelta < 1 or scelta > len(f):
                print("Numero film non valido")
                corretto = False
            else:
                return scelta  
        except:
            print("Formato numero film non valido")
            
            corretto = False
 

def modificaFilm(f):
    visualizzaFilm(f)
    posizione = chiediPosizione(f)
    nome = chiediFilm()
    f[posizione-1] = nome

def visualizzaFilm(f):
    if len(f) == 0:
        print("Nessun film in archivio")
    else:
        for i,f in enumerate(f):
            print(f"{i+1} - {f}")
 
film = []
 
film=Carica()
 
fine = False
while not fine:
    stampaMenu()
    s = scelta()
    if s == 1:
        n = inserisciFilm(film)
    elif s == 2:
        visualizzaFilm(film)
    elif s == 3:
        modificaFilm(film)
    elif s == 4:
        eliminaFilm(film)
    elif s == 0:
        Salva(film)
        print("Arrivedorciiiii")
        fine = True
   