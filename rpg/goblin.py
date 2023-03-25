from monstro import Monstro

# Define a classe Goblin como uma subclasse de Monstro
class Goblin(Monstro):
    def __init__(self,tipo,pontos_vida,pontos_atk,inteligencia):
        super().__init__(tipo,pontos_vida,pontos_atk)  
        self.inteligencia = inteligencia