from conta import Conta

class ContaCorrente(Conta):
    def __init__(self, id_conta: int, saldo: float, limite: float):
        super().__init__(id_conta, saldo)
        self.limite = limite
        self.limite_atual = limite
    
    def sacar(self, valor: float) -> bool:
        if self.saldo >= valor:
            self.saldo -= valor
            return True
        elif self.saldo + self.limite_atual >= valor:
            self.limite_atual -= valor - self.saldo
            self.saldo -= valor
            return True
        else:
            print("---------------------------------------------------------------")
            print(f"Saldo insuficiente.\nSeu saldo atual é: R${self.saldo} + Limite: R${self.limite_atual}.")
            print("---------------------------------------------------------------")
            return False
    
    def depositar(self, valor: float) -> None:
        if self.saldo < 0:
            self.limite_atual += abs(self.saldo)
        self.saldo += valor
