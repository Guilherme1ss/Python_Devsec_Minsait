from servivo import SerVivo

# Define a classe Personagem como uma subclasse de SerVivo
class Personagem(SerVivo):
    def __init__(self, nome, pontos_vida, pontos_atk):
        super().__init__(pontos_vida, pontos_atk)   
        self.nome = nome
