class Sistema:
    def get_nome(self): # Função que verifica se a classe tem o atributo 'nome'
        if hasattr(self, 'nome'):
            return self.nome
        else:
            return self.__class__.__name__
        
    def resultado(self, alvo):
        if alvo.pontos_vida > 0:  # Verifica se o alvo ainda está vivo após o ataque
            print(f"O {Sistema.get_nome(self)} causou {self.pontos_atk} de dano no {Sistema.get_nome(alvo)}. O {Sistema.get_nome(alvo)} agora tem {alvo.pontos_vida} ponto(s) de vida.")
        else:
            print(f"O {Sistema.get_nome(self)} causou {self.pontos_atk} de dano no {Sistema.get_nome(alvo)} e o matou.") 