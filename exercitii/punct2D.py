import math


class Punct2D:
    def __init__(self, denumire:str, coordonataX: float, coordonataY:float):
        self.denumire = denumire
        self.coordonataX = coordonataX
        self.coordonataY = coordonataY


    def get_denumire(self):
        return self.denumire

    def set_denumire(self, denumire:str):
        self.denumire = denumire

    def get_X(self):
        return self.coordonataX;

    def set_X(self, cX: float):
        self.coordonataX = cX

    def get_Y(self):
        return self.coordonataY;

    def set_Y(self, cY: float):
        self.coordonataY = cY

    def toString(self):
        return f"{self.denumire} ( {self.coordonataX} , {self.coordonataY} )"

    def distanțaPânăLaOrigine(self):
        return math.sqrt(self.coordonataX ** 2 + self.coordonataY ** 2)

# Exemplu de utilizare
punct = Punct2D("A", 2.0, 3.0)
print(punct.toString())  # Output: A(2.0, 3.0)
print(f"Distanța până la origine: {punct.distanțaPânăLaOrigine()}")  # Output: Distanța până la origine: 3.61