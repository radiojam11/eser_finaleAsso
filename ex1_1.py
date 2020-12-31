"""
1 Prova Finale IFTS - Python - 22 Dicembre 2020
1.1 Esercizio
• Scrivere una classe Articolo che abbia come attributi un nome (string) ed un valore (int) in
Euro
• Scrivere una classe Pacco che abbia come attributi il destinatario del pacco ed un codice e gli
articoli che contiene (lista)
– aggiungere un metodo per aggiungere Articoli al pacco
– aggiungere un metodo per calcolare il valore del pacco
"""

class Articolo():
    def __init__(self, nome="Nome del Articolo", valore=1 ):
        self.nome=nome
        self.valore=valore
        
class Pacco():
    def __init__(self, contenuto=[], destinatario="via e citta", codice=123):
        self.destinatario=destinatario
        self.codice=codice
        self.contenuto=contenuto

    def aggiungi_articolo(self, art ):
        self.contenuto.append(art)
        print("aggiunto articolo :", art.nome)

    def prezzo_pacco(self):
        prezzo=0
        for el in self.contenuto:
            prezzo += el.valore
        return prezzo



panettone = Articolo(nome="Panettone", valore=13)
spumante = Articolo(nome="Ferrari", valore = 23)
regalo = Articolo(nome="Regalino", valore = 100)

paccodiMario = Pacco(contenuto=[panettone, spumante], destinatario="Roma via Versi 22", codice=19555)
print(paccodiMario.prezzo_pacco())
paccodiMario.aggiungi_articolo(regalo)
print(paccodiMario.prezzo_pacco())


