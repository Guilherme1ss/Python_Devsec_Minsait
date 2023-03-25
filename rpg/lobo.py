from monstro import Monstro

# Define a classe Lobo como uma subclasse de Monstro
class Lobo(Monstro):
    def __init__(self, tipo, pontos_vida, pontos_atk, força):
        super().__init__(tipo,pontos_vida,pontos_atk)  
        self.força = força 