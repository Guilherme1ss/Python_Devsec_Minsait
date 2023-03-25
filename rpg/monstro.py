from servivo import SerVivo

# Define a classe Monstro como uma subclasse de SerVivo 
class Monstro(SerVivo):
    def __init__(self, tipo, pontos_vida, pontos_atk):
        super().__init__(pontos_vida, pontos_atk)
        self.tipo = tipo