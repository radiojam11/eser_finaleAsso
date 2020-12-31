"""1.4 Esercizio
• Scrivere una funzione che dato un numero restituisca True se il numero è primo, False in caso
contrario.
• Scrivere il relativo main che testi la funzione per i primi 100 numeri
nota: un numero è primo quando è divisibile solo per 1 e per sé stesso

"""

def controlla_numero(num):
    cont = 0
    if num==2:
        return False
    for i in range (2, num, 1):
        if num%i == 0:
            cont +=1
    if cont == 0:
        return True
    else:
        return False

for i in range (1,100):
    print("controllo il numero ",i, ",sara' un numero primo?", controlla_numero(i))

