"""
1.2 Esercizio
• Scrivere una classe quadrilatero che rappresenta una figura geometrica con 4 lati
– definire gli attributi della classe
– definire un metodo che calcoli il perimetro
– definire un metodo che confronti il perimetro del quadrilatero con un secondo perimetro
(passare l’oggetto quadrilatero come parametro) e restituisca come uscita il risultato del
confronto
– scrivere nel main il codice che provi che la classe funzioni correttamente
• Estendere la classe quadrilatero con una classe rettangolo
– aggiungere eventuali attributi necessari
– aggiungere un metodo che calcoli l’area del rettangolo

– scrivere nel main il codice che provi il suo corretto funzionamento (incluso quanto ered-
itato dalla classe quadrilatero)

• estendere la classe quadrilatero con una classe rombo (l1 = l2 = l3 = l4)
– aggiungere eventuali attributi necessari
– aggiungere un metodo che calcoli l’area del rombo
vedi pdf

– aggiungere un metodo per il calcolo della diagonale 1 dato il lato e l’altra diagonale 2
vedi pdf

– scrivere nel main il codice che provi il suo corretto funzionamento (incluso quanto ered-
itato dalla classe quadrilatero)

"""
from math import sqrt

class Quadrilatero():
    def __init__(self, l1=1,l2=1,l3=1,l4=1):
        self.l1=l1
        self.l2=l2
        self.l3=l3
        self.l4=l4
    def perimetro(self,l1=1,l2=1,l3=1,l4=1):
        perim=self.l1+self.l2+self.l3+self.l4
        return perim
    def confronta(self, quad2):
        res = self.perimetro()-quad2.perimetro()
        return res

class Rettangolo(Quadrilatero):
    def __init__(self,l1=1,l2=1):
        super().__init__(l1,l2)
        self.l1
        self.l2
    def area_rett(self):
        area= self.l1*self.l2
        return area

class Rombo(Quadrilatero):
    def __init__(self,l1=1, d2=1):
        super().__init__(l1)
        self.d2=d2
        if d2 > self.l1*2:
            print("ha sbagliato la misura")
            self.d2=self.l1
        self.l1=l1
        
    
    def calcolo_diagonale(self):
        d1 = 2*(sqrt((self.l1**2)-(self.d2**2)/2))
        return d1

    def area_rombo(self):
        arear = (self.calcolo_diagonale()*self.d2)/2 
        return arear
       

    


quad1 = Quadrilatero(2,3,4,3)
quad2 = Quadrilatero(3,3,4,5)

print(quad1.confronta(quad2))

ret1 = Rettangolo(10,12)
print(ret1.area_rett())

rombo1 = Rombo(10,14)

print(rombo1.area_rombo())
print(rombo1.calcolo_diagonale())