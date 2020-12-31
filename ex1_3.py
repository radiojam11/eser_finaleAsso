"""
1.3 Esercizio
• Scrivere un programma python che consenta di conservare le temperature delle città; In
particolare scrivere le seguenti funzioni:
– Inserimento di una nuova città
– Cancellazione di una città
– Modifica della temperatura di una città
– Ricerca di una città dato il nome
– Elenco di tutte le città con le relative temperature

"""
temperature = {}
def inserisci_citta(citta, temp):
    temperature[citta]=temp

def cancella_citta(citta):
    del temperature[citta]

def mod_temp_citta(citta, temp):
    temperature[citta]=temp

def cerca_citta(citta):
    if citta in temperature:
        print("Nella citta "+ citta+" oggi ci sono "+ str(temperature[citta])+" gradi centigradi")
    else:
       print(" la citta richiesta non e' monitorata")
def elenco_citta():
    for el in temperature:
        print( "Citta di " + el + " Temperatura registrata = ", temperature[el])


inserisci_citta("Roma", 25)
inserisci_citta("Chieti", 20)
inserisci_citta("Fermo", 21)
inserisci_citta("Canicatti", 33)

cancella_citta("Canicatti")
mod_temp_citta("Roma", 44)

cerca_citta("Fermo")

elenco_citta()
