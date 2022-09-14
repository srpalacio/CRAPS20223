import random

class Dado:
    #metodo constructor
    def __init__(self):
        self.valor=0

    def girar(self):
        self.valor=random.randit(1,6)

    def getValor(self):
        return self.valor