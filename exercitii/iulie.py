from abc import ABC, abstractmethod
import math

class FormaGeometrica(ABC):
    def __init__(self, nume:str):
        self._nume = nume

    @abstractmethod
    def aria(self) -> float:
        pass

    def get_nume(self):
        return self._nume

    def set_nume(self, nume1):
        self._nume = nume1

class Patrat(FormaGeometrica):
    def __init__(self, nume:str, latura:float):
        super().__init__(nume)
        self._latura = latura

    def aria(self) -> float:
        return self._latura **2

class Cerc(FormaGeometrica):
    def __init__(self, nume:str, raza:float):
        super().__init__(nume)
        self._raza = raza

    def aria(self)->float:
        return math.pi * (self._raza**2)



patrat = Patrat("patrat1", 5)
print(f"{patrat.get_nume()} {patrat.aria()}")

cerc = Cerc("cerc1", 7)
print(f"{cerc.get_nume()} {cerc.aria()}")


#CREARE VECTOR
vector = [
    Patrat("patrat2", 7.0),
    Cerc("cerc2", 8.1),
    Patrat("patrat3", 5.3)
]

x = float(input())
for forma in vector:
    if   forma.aria() > x:
        print(f"{forma._nume()} {forma.aria()}")


#void sorting(vector<FormaGeometrica*>& v) {
#    bool ok = 0;
#    while (!ok) {
#        ok = 1;
#        for (size_t i = 0; i < v.size()-1; i++) {
#            if (v[i]->aria() > v[i + 1]->aria()) {
#                swap(v[i], v[i + 1]);
#                ok = 0;
#            }
#       }
#    }
#}
#