class Banco:
    def __init__(self):
        self.contas = {}

    def cadastrar_conta(self, conta):
        self.contas[conta.id_conta] = conta
        self.buscar_conta_por_id(conta.id_conta)

    def buscar_conta_por_id(self, id_conta):
        if not conta:
            raise ValueError(f"Conta com id {id_conta} não encontrada.")
        return conta

    def transferir_valor(self, id_conta_origem, id_conta_destino, valor):
        conta_origem = self.buscar_conta_por_id(id_conta_origem)
        conta_destino = self.buscar_conta_por_id(id_conta_destino)
        if conta_origem is not None and conta_destino is not None:
            if conta_origem.saldo >= valor:
                conta_origem.sacar(valor)
                conta_destino.depositar(valor)
                print(f"Transferência de R${valor:.2f} da conta {id_conta_origem} para a conta {id_conta_destino} realizada com sucesso.")
            else:
                print(f"Saldo insuficiente na conta {id_conta_origem} para realizar a transferência.")
        else:
            print("Não foi possível realizar a transferência.")