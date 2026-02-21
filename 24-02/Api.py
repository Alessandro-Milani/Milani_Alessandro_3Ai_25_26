#Utilizzando le API pubbliche documentate al sito https://fakeapi.net/docs/fake-e-commerce-api realizzare un programma Python che funziona nella seguente maniera:
#all'avvio il programma mostra l'elenco delle categorie di prodotti, usando l'api https://fakeapi.net/products/categories. Mostrare nel formato "progressivo numerico - nome categoria".
#Progressivo numerico è un numero progressivo che parte da 1

#Mostrate tutte le categorie, il programma chiede quale categoria si intende visualizzare. Effettuati i dovuti controlli, vengono visualizzati solo gli articoli di quella 
#specifica categoria. A tale scopo usare l'api https://fakeapi.net/products/category/....  [al posto dei puntini bisogna mettere il nome della categoria scelta,
#ad esempio https://fakeapi.net/products/category/accessories.
#Dei prodotti va mostrato l'id, il nome ed il prezzo. 

#A quel punto il programma chiede se si vuole vedere il dettaglio di un singolo prodotto oppure tornare all'inizio (scelta categorie).
#Per visualizzare il dettaglio di un prodotto occorrerà chiamare il servizio https://fakeapi.net/products/.... [al posto dei puntini bisogna mettere l'id del prodotto, 
#ad esempio https://fakeapi.net/products/1 ] 

#Nel dettaglio mostrare  id, nome, prezzo, descrizione estesa, categoria e brand.
#Alla fine si ritorna sempre all'elenco delle categorie e si riparte

import requests

def categorie():
    response = requests.get("https://fakeapi.net/products/categories")
    if response.status_code != 200:
        print("Errore nel recupero delle categorie.")
    else:
        categorie=response.json() # è un metodo della libreria requests che converte automaticamente la risposta JSON (testo) ricevuta da una richiesta HTTP in un dizionario o una lista Python strutturata. Permette di elaborare facilmente i dati provenienti da API web, trasformando stringhe JSON in oggetti manipolabili.
        for i,categoria in enumerate(categorie):
            print(f"{i+1} - {categoria}")
        return categorie

def richiesta_utente(categorie):
    errore=True
    while errore:

        scelta=input("inserisci il nome della categoria che vuoi visualizzare: ")
        if scelta in categorie:
            errore=False
        else:
            print("Scelta non valida. Riprova.")
    return scelta

def Lista_Prodotti(scelta):
        lista_id=[]
        response = requests.get(f"https://fakeapi.net/products/category/{scelta}")
        if response.status_code != 200:
            print("Errore nel recupero dei prodotti della categoria selezionata.")
        else:
            prodotti = response.json()
            for prodotto in prodotti["data"]:
                print(f"ID: {prodotto['id']}, Nome: {prodotto['title']}, Prezzo: {prodotto['price']}")
                lista_id.append(prodotto["id"])
            # print(prodotti["data"][0]["id"])
            return lista_id
            
def Scelta():
    errore=True
    while errore:
        scelta=input("Vuoi vedere il dettaglio di un prodotto? (s/n): ")
        if scelta.lower() == "s" or scelta.lower() == "n":
            errore=False
        else:
            print("Scelta non valida. Riprova.")
    return scelta

def scelta_id(lista_id):
    errore=True
    while errore:
        try:
            id_scelto=int(input("Inserisci l'ID del prodotto di cui vuoi vedere il dettaglio: "))
        
            if id_scelto in lista_id:
                errore=False
                return id_scelto
            else:
                print("ID non valido. Riprova.")
        except:
            print("Inserisci un numero valido.")

def dettaglio_prodotto(id_scelto):
    response = requests.get(f"https://fakeapi.net/products/{id_scelto}")
    if response.status_code != 200:
        print("Errore nel recupero del dettaglio del prodotto.")
    else:
        prodotto = response.json()
        print(f"ID: {prodotto['id']}, Nome: {prodotto['title']}, Prezzo: {prodotto['price']}, Descrizione: {prodotto['description']}, Categoria: {prodotto['category']}, Brand: {prodotto['brand']}")
    
while True:
    elenco_categorie=categorie()
    scelta=richiesta_utente(elenco_categorie)
    lista_id=Lista_Prodotti(scelta)
    risposta=Scelta()
    if risposta.lower()=="s":
        id_scelto=scelta_id(lista_id)
        dettaglio_prodotto(id_scelto)
