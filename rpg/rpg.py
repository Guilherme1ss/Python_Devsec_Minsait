from personagem import Personagem
from lobo import Lobo
from goblin import Goblin

# Cria os objetos das classes
personagem = Personagem(nome="Herói", pontos_vida= 10, pontos_atk= 2)
goblin = Goblin(tipo="Goblin", pontos_vida=5, pontos_atk= 1, inteligencia= 2)
lobo = Lobo(tipo="Lobo",pontos_vida= 3, pontos_atk= 4, força= 7)


# Ataques

lobo.atacar(personagem)
lobo.atacar(personagem)
lobo.atacar(personagem)
lobo.atacar(personagem)

goblin.atacar(lobo)

personagem.atacar(lobo)