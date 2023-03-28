from conta import Conta
from banco import Banco
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


class ContaCorrente(Conta, Banco):
    def __init__(self, id_conta: int, saldo: float, limite: float, banco: Banco, nome_do_usuario: str):
        super().__init__(id_conta, saldo)
        self.limite = limite
        self.limite_atual = limite

        self.extrato = []

        self.banco = banco
        self.contas_corrente = banco.contas_corrente
        self.banco.cadastrar_conta_corrente(
            conta=self, nome=nome_do_usuario, tipo='Conta Corrente')

    def gerenciador_de_caso(self, valor):
        if self.saldo >= valor:
            self.caso = 1
            return self.caso
        elif self.saldo + self.limite_atual >= valor:
            self.caso = 2
            return self.caso
        elif self.limite_atual >= valor:
            self.caso = 3
            return self.caso
        else:
            self.caso = 4
            return self.caso

    def sacar(self, valor):
        self.caso = self.gerenciador_de_caso(valor)
        if self.caso == 1:
            self.saldo -= valor
            self.exibir_saque(valor=valor)
            self.extrato.append(
                f"Saque de {locale.currency(valor, grouping=True)}")
            return True
        elif self.caso == 2:
            self.saldo -= valor
            self.limite_atual += self.saldo
            self.exibir_saque(valor=valor)
            self.extrato.append(
                f"Saque de {locale.currency(valor, grouping=True)}")
            return True
        elif self.caso == 3:
            self.saldo -= valor
            self.limite_atual -= valor
            self.exibir_saque(valor=valor)
            self.extrato.append(
                f"Saque de {locale.currency(valor, grouping=True)}")
            return True
        else:
            self.__saldo_insuficiente(valor)
            return False

    def exibir_saque(self, valor):
        print("---------------------------------------------------------------")
        print(f"Você sacou {locale.currency(valor, grouping=True)}.\nO seu saldo atual da conta corrente é: {locale.currency(self.saldo, grouping=True)} + Limite da conta: {locale.currency(self.limite_atual, grouping=True)}")
        print("---------------------------------------------------------------")

    def exibir_deposito(self, valor):
        print("---------------------------------------------------------------")
        print(f"Você depositou {locale.currency(valor, grouping=True)}\nO seu saldo atual da conta corrente é: {locale.currency(self.saldo, grouping=True)} + Limite da conta: {locale.currency(self.limite_atual, grouping=True)}")
        print("---------------------------------------------------------------")

    def __saldo_insuficiente(self, valor) -> None:
        print("---------------------------------------------------------------")
        print(
            f"Saldo insuficiente.\nVocê não possui {locale.currency(valor, grouping=True)} em sua conta.\nSeu saldo atual é: {locale.currency(self.saldo, grouping=True)} + Limite: {locale.currency(self.limite_atual, grouping=True)}.")
        print("---------------------------------------------------------------")

    def exibir_extrato(self):
        print("---------------------------------------------------------------")
        print('EXTRATO:\n')
        for indice, elemento in enumerate(self.extrato):
            print(indice + 1, '-', elemento)
        print(f'\nSaldo atual: {locale.currency(self.saldo, grouping=True)}')
        print("---------------------------------------------------------------")

    def depositar(self, valor: float) -> None:
        if self.saldo < 0:
            self.limite_atual += abs(self.saldo)
        self.saldo += valor
        self.exibir_deposito(valor=valor)
        self.extrato.append(
            f"Depósito de {locale.currency(valor, grouping=True)}")

    def transferir(self, valor: float, id_conta_destino: int):
        self.transferir_valor(id_conta_origem=self.id_conta,
                              id_conta_destino=id_conta_destino, valor=valor)
