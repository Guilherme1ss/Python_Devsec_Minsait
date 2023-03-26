from typing import Dict
from typing import Union
from contaCorrente import ContaCorrente
from contaPoupanca import ContaPoupanca

class Banco:
    def __init__(self):
        self.contas: Dict[int, Union[ContaCorrente, ContaPoupanca]] = {}

    def adicionar_conta(self, conta: Union[ContaCorrente, ContaPoupanca]) -> None:
        self.contas[conta.id_conta] = conta

    def transferir(self, id_origem: int, id_destino: int, valor: float) -> bool:
        if id_origem not in self.contas or id_destino not in self.contas:
            print("Erro: Conta de origem ou destino não encontrada.")
            return False

        conta_origem = self.contas[id_origem]
        conta_destino = self.contas[id_destino]

        if not isinstance(conta_origem, ContaCorrente) or not isinstance(conta_destino, ContaCorrente):
            print("Erro: Transferência não permitida para contas de poupança.")
            return False

        if conta_origem.saldo + conta_origem.limite_atual < valor:
            print("Erro: Saldo insuficiente para realizar a transferência.")
            return False

        conta_origem.sacar(valor)
        conta_destino.depositar(valor)
        return True
