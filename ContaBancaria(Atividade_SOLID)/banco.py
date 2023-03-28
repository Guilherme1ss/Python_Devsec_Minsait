class Banco:
    def __init__(self):
        self.contas_corrente = {}
        self.contas_poupanca = {}

    def cadastrar_conta_corrente(self, conta, nome, tipo):
        self.contas_corrente[conta.id_conta] = [conta, nome, tipo]
        self.buscar_conta_por_id(conta.id_conta)
        print(self.contas_corrente)

    def cadastrar_conta_poupanca(self, conta, nome, tipo):
        self.contas_poupanca[conta.id_conta] = [conta, nome, tipo]
        self.buscar_conta_por_id(conta.id_conta)
        print(self.contas_poupanca)

    def buscar_conta_por_id(self, id_conta):
        conta = self.contas_corrente.get(id_conta)
        if not conta:
            raise ValueError(f"Conta com id {id_conta} não encontrada.")
        return conta
    
    def buscar_nome_da_conta(self, id_conta_origem, id_conta_destino):
        nome_conta_origem = self.contas_corrente[id_conta_origem][1]
        nome_conta_destino = self.contas_corrente[id_conta_destino][1]
        return nome_conta_origem, nome_conta_destino

    def transferir_valor(self, id_conta_origem, id_conta_destino, valor):
        conta_origem = self.buscar_conta_por_id(id_conta_origem)
        conta_destino = self.buscar_conta_por_id(id_conta_destino)
        nome_conta_origem, nome_conta_destino = self.buscar_nome_da_conta(id_conta_origem=id_conta_origem, id_conta_destino=id_conta_destino)
        if conta_origem is not None and conta_destino is not None:
            if conta_origem[0].saldo >= valor:
                conta_origem[0].sacar(valor)
                conta_destino[0].depositar(valor)
                print(f"Transferência de R${valor:.2f} da conta de {nome_conta_origem} para a conta de {nome_conta_destino} realizada com sucesso.")
            else:
                print(f"Saldo insuficiente na conta {id_conta_origem} para realizar a transferência.")
        else:
            print("Não foi possível realizar a transferência.")

