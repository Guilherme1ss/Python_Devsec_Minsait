def get_nome(obj): # Função que verifica se a classe tem o atributo 'Nome'
    if hasattr(obj, 'nome'):
        return obj.nome
    else:
        return obj.__class__.__name__

class SerVivo:
    
    def __init__(self, pontos_vida, pontos_atk):
        self.pontos_vida = pontos_vida 
        self.pontos_atk = pontos_atk 

    def atacar(self, alvo): 
        if self.pontos_vida <= 0:  # Verifica se o objeto que está atacando está vivo
            print(f'O {get_nome(self)} não pode atacar o {get_nome(alvo)}, pois o {get_nome(self)} está morto.')
            return
        else:
            if alvo.pontos_vida > 0:  # Verifica se o alvo do ataque está vivo
                alvo.pontos_vida -= self.pontos_atk  # Subtrai os pontos de ataque do objeto que está atacando dos pontos de vida do alvo
                self.resultado(alvo)  # Chama o método resultado para imprimir informações sobre o resultado do ataque
            else:
                print(f'O {get_nome(alvo)} está morto.')

    def resultado(self, alvo):
        if alvo.pontos_vida > 0:  # Verifica se o alvo ainda está vivo após o ataque
            print(f"O {get_nome(self)} causou {self.pontos_atk} de dano no {get_nome(alvo)}. O {get_nome(alvo)} agora tem {alvo.pontos_vida} ponto(s) de vida.")
        else:
            print(f"O {get_nome(self)} causou {self.pontos_atk} de dano no {get_nome(alvo)} e o matou.") 

# Define a classe Personagem como uma subclasse de SerVivo
class Personagem(SerVivo):
    def __init__(self, nome, pontos_vida, pontos_atk):
        super().__init__(pontos_vida, pontos_atk)   
        self.nome = nome

# Define a classe Monstro como uma subclasse de SerVivo 
class Monstro(SerVivo):
    def __init__(self, tipo, pontos_vida, pontos_atk):
        super().__init__(pontos_vida, pontos_atk)
        self.tipo = tipo

# Define a classe Monstro como uma subclasse de SerVivo 
class Monstro(SerVivo):
    def __init__(self, tipo, pontos_vida, pontos_atk):
        super().__init__(pontos_vida,pontos_atk)  
        self.tipo = tipo 

# Define a classe Lobo como uma subclasse de Monstro
class Lobo(Monstro):
    def __init__(self, tipo, pontos_vida, pontos_atk, força):
        super().__init__(tipo,pontos_vida,pontos_atk)  
        self.força = força  

# Define a classe Goblin como uma subclasse de Monstro
class Goblin(Monstro):
    def __init__(self,tipo,pontos_vida,pontos_atk,inteligencia):
        super().__init__(tipo,pontos_vida,pontos_atk)  
        self.inteligencia = inteligencia 

# Cria os objetos das classes
personagem = Personagem("Herói",10,2)
goblin = Goblin("Goblin",5,1,2)
lobo = Lobo("Lobo",3,4,7)


# Ataques

lobo.atacar(personagem)
lobo.atacar(personagem)
lobo.atacar(personagem)
lobo.atacar(personagem)

goblin.atacar(lobo)

personagem.atacar(lobo)