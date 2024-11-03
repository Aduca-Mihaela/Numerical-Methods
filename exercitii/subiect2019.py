import math


class Punct2D:
    def __init__(self, denumire:str, coordonataX:float, coordonataY:float):
        self._denumire = denumire
        self._coordonataX = coordonataX
        self._coordonataY = coordonataY

    def distanta(self):
        return math.sqrt(self._coordonataX ** 2 + self._coordonataY ** 2)

    def getInfo(self):
        return f"{self._denumire} {self.distanta()}"

    def __str__(self):
        return f"{self._denumire} {self._coordonataX} {self._coordonataY}"

class ListaDePuncte:
    def __init__(self):
        self.__puncte = []

    def getPuncte(self):
        return self.__puncte

    def adauga(self, p):
        if p not in self.__puncte:
            self.__puncte.append(p)


    def filtruPuncte(self, limita:float):
        for punct in self.__puncte:
            if punct.distanta() <= limita:
                self.__puncte.pop(punct)

    def sortare(self):
       return self.__puncte.sort(key= lambda punct: punct._denumire)

lista = ListaDePuncte()

lista.adauga(Punct2D("Z", 1, 2))
lista.adauga(Punct2D("B", 3, 4))

def afisareLista(lista):
    for i in lista.getPuncte():
        print(i)

lista.sortare()
afisareLista(lista)


def prelucrare1():
    lista = ListaDePuncte()
    lista.adauga(Punct2D("C",1,2))
    lista.adauga(Punct2D("A", 2, 3))
    lista.adauga(Punct2D("B", 1, 2))
    lista.adauga(Punct2D("E", 2, 4))
    lista.adauga(Punct2D("D", 2, 5))
    lista.sortare()
    afisareLista(lista)

#prelucrare1()


class Punct3D(Punct2D):
    def __init__(self, denumire:str,coordonataX:float, coordonataY:float, coordonataZ:float):
        super().__init__(denumire, coordonataX, coordonataY)
        self.__coordonataZ = coordonataZ

    def distanta(self):
        return math.sqrt(self._coordonataX ** 2 + self._coordonataY ** 2 + self.__coordonataZ**2)

    def getInfo(self):
        return f"{self._denumire} {self.distanta()}"

def prelucrare2(val):
    lista = ListaDePuncte()
    lista.adauga(Punct2D("A",1,2))
    lista.adauga(Punct3D("B", 1, 2, 3))
    lista.adauga(Punct2D("C", 1, 2))
    lista.adauga(Punct3D("D",3, 4, 5))
    afisareLista(lista)


prelucrare2(1)