from sistema import Sistema

class SerVivo:
    
    def __init__(self, pontos_vida, pontos_atk):
        self.pontos_vida = pontos_vida 
        self.pontos_atk = pontos_atk 

    def atacar(self, alvo): 
        if self.pontos_vida <= 0:  # Verifica se o objeto que está atacando está vivo
            print(f'O {Sistema.get_nome(self)} não pode atacar o {Sistema.get_nome(alvo)}, pois o {Sistema.get_nome(self)} está morto.')
            return
        else:
            if alvo.pontos_vida > 0:  # Verifica se o alvo do ataque está vivo
                alvo.pontos_vida -= self.pontos_atk  # Subtrai os pontos de ataque do objeto que está atacando dos pontos de vida do alvo
                Sistema.resultado(self, alvo)  # Chama o método resultado para imprimir informações sobre o resultado do ataque
            else:
                print(f'O {Sistema.get_nome(alvo)} já está morto.') # Mostra mensagem caso o alvo já esteja morto.