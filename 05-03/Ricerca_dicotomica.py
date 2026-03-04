#restituisce true se l'elemento cercato è nella lista, False altrimenti
def RicercaDicotomica(lista, numero_da_cercare):
    i = 0
    f = (len(lista)-1)
   
    while i!=f or lista[m]==numero_da_cercare:
   
        m = (i+f)//2
 
        if lista[m] == numero_da_cercare:
            return True
        if lista[m] > numero_da_cercare:
            f=m
        elif lista[m] < numero_da_cercare:
            i=m
    return False
 
 
lista=[10,12,44,72,88,96,104,1000]
 
print(RicercaDicotomica(lista, 88))