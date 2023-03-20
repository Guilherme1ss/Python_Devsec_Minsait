class UrnaEletronica:
    def __init__(self):
        self.candidatos = [{'nome_candidato': 'Nome', 'partido': 'Partido'}]

    def exibe_candidatos(self): # exibe lista completa de candidatos
        for candidato in self.candidatos:
            print('--------------------------------')
            print(f"Nome do candidato: {candidato['nome_candidato']}")
            print(f"Partido: {candidato['partido']}")
            print('--------------------------------')
    
    def novo_candidato(self, nome, partido): # adiciona um novo candidato a lista
        novo_candidato = {'nome_candidato': nome, 'partido': partido}
        self.candidatos.append(novo_candidato)


    def remove_ultimo_candidato(self):
        self.candidatos.pop()

    def atualizar_candidato(self, indice, chave, valor): # atualiza lista de candidatos através do índice e da chave.
        try:
            self.candidatos[indice][chave] = valor
        except IndexError:
            print('Índice inválido')
        except KeyError:
            print('Chave inválida')

# Cria o objeto da classe
urna = UrnaEletronica()

# Define a lista inicial de candidatos.
urna.candidatos = [
    {'nome_candidato': 'Guilherme', 'partido': 'PDP'},
    {'nome_candidato': 'João', 'partido': 'UPQS'}
]


# Ações a serem tomadas

urna.remove_ultimo_candidato()
urna.novo_candidato('Pedro', 'PLL')
urna.atualizar_candidato(0, 'partido', 'OIP')
urna.exibe_candidatos()