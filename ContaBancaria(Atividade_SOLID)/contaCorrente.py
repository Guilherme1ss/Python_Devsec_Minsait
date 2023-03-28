from conta import Conta
from banco import Banco

class ContaCorrente(Conta, Banco):
    def __init__(self, id_conta: int, saldo: float, limite: float, banco: Banco):
        super().__init__(id_conta, saldo)
        self.limite = limite
        self.limite_atual = limite
        self.extrato = []
        self.banco = banco
        self.banco.cadastrar_conta(conta= self)
        
    
    def sacar(self, valor: float) -> bool:
        if self.pode_sacar(valor):
            if self.saldo >= valor:
                self.saldo -= valor
                self.exibir_saque(valor= valor)
                self.extrato.append(f"Saque de R${valor:.2f}")
            elif self.saldo + self.limite_atual >= valor:
                self.saldo -= valor
                self.limite_atual += self.saldo
                self.exibir_saque(valor= valor)
                self.extrato.append(f"Saque de R${valor:.2f}")
            elif self.limite_atual >= valor:
                self.saldo -= valor
                self.limite_atual -= valor
                self.exibir_saque(valor= valor)
                self.extrato.append(f"Saque de R${valor:.2f}")
            return True
        else:
            self.__saldo_insuficiente(valor)
            return False
        
    def pode_sacar(self, valor: float) -> bool:
        return self.saldo >= valor or self.saldo + self.limite_atual >= valor or self.limite_atual >= valor
    
    def exibir_saque(self, valor):
        print("---------------------------------------------------------------")
        print(f"Você sacou R${valor:.2f}.\nO seu saldo atual da conta corrente é: R${self.saldo:.2f} + Limite da conta: R${self.limite_atual:.2f}")
        print("---------------------------------------------------------------")

    def exibir_deposito(self, valor):
        print("---------------------------------------------------------------")
        print(f"Você depositou R${valor:.2f}.\nO seu saldo atual da conta corrente é: R${self.saldo:.2f} + Limite da conta: R${self.limite_atual:.2f}")
        print("---------------------------------------------------------------")

    def __saldo_insuficiente(self, valor) -> None:
        print("---------------------------------------------------------------")
        print(f"Saldo insuficiente.\nVocê não possui R${valor:.2f} em sua conta.\nSeu saldo atual é: R${self.saldo} + Limite: R${self.limite_atual:.2f}.")
        print("---------------------------------------------------------------")

    def exibir_extrato(self):
        print("---------------------------------------------------------------")
        print('EXTRATO:\n')
        for indice, elemento in enumerate(sorted(self.extrato)):
            print(indice + 1,'-', elemento)
        print(f'\nSaldo atual: R${self.saldo}')
        print("---------------------------------------------------------------")
    
    def depositar(self, valor: float) -> None:
        if self.saldo < 0:
            self.limite_atual += abs(self.saldo)
        self.saldo += valor
        self.exibir_deposito(valor= valor)
        self.extrato.append(f"Depósito de R${valor:.2f}")
