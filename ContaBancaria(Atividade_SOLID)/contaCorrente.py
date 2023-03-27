from conta import Conta

class ContaCorrente(Conta):
    def __init__(self, id_conta: int, saldo: float, limite: float):
        super().__init__(id_conta, saldo)
        self.limite = limite
        self.limite_atual = limite

    
    def sacar(self, valor: float) -> bool:
        if self.saldo >= valor:
            self.saldo -= valor
            self.exibir_saldo()
            return True
        elif self.saldo + self.limite_atual >= valor:
            self.limite_atual -= valor - self.saldo
            self.saldo -= valor
            self.exibir_saldo()
            return True
        else:
            self.__saldo_insuficiente(valor)
            return False
        
    def exibir_saldo(self):
        print("---------------------------------------------------------------")
        print(f"Saldo atual da conta corrente: R${self.saldo:.2f} + Limite da conta: R${self.limite_atual:.2f}")
        print("---------------------------------------------------------------")

    def __saldo_insuficiente(self, valor) -> None:
        print("---------------------------------------------------------------")
        print(f"Saldo insuficiente.\nVocê não possui R${valor:.2f} em sua conta.\nSeu saldo atual é: R${self.saldo} + Limite: R${self.limite_atual:.2f}.")
        print("---------------------------------------------------------------")
    
    def depositar(self, valor: float) -> None:
        if self.saldo < 0:
            self.limite_atual += abs(self.saldo)
            self.saldo += valor
            self.exibir_saldo()
