from conta import Conta
from datetime import timedelta

class ContaPoupanca(Conta):
    def __init__(self, id_conta: int, saldo: float, taxa_juros_anual: float):
        super().__init__(id_conta, saldo)
        self.taxa_juros_anual = taxa_juros_anual

    def sacar(self, valor: float):
        if self.saldo >= valor:
            self.saldo -= valor
            self.exibir_saldo()
        else:
            self.__saldo_insuficiente()

    def exibir_saldo(self):
        print("---------------------------------------------------------------")
        print(f"Saldo atual da conta poupança é: R${self.saldo:.2f}")
        print("---------------------------------------------------------------")

    def __saldo_insuficiente(self) -> None:
        print("---------------------------------------------------------------")
        print(f"Saldo insuficiente.\nSeu saldo atual é: R${self.saldo:.2f}")
        print("---------------------------------------------------------------")

    def depositar(self, valor: float, segundos: int = 0, minutos: int = 0, horas: int = 0, dias: int = 0, meses: int = 0, anos: int = 0):
        self.calcular_tempo_total(segundos= segundos, minutos= minutos, horas= horas, dias= dias, meses= meses, anos= anos)
        self.calcular_rendimento(tempo_deposito= self.tempo_deposito.total_seconds(), valor_deposito= valor)
        self.exibir_saldo()
        

    def calcular_tempo_total(self, segundos, minutos, horas, dias, meses, anos):
        self.media_dias_em_mes = 365/12
        self.total_dias = dias + meses*self.media_dias_em_mes + anos*365
        self.tempo_deposito = timedelta(seconds=segundos, minutes=minutos, hours=horas, days=self.total_dias)
        

    def calcular_rendimento(self, tempo_deposito: int, valor_deposito: float):
        anos = tempo_deposito / (365 * 24 * 60 * 60)
        taxa_juros_anual = self.taxa_juros_anual / 100
        rendimento = valor_deposito * ((1 + taxa_juros_anual) ** anos - 1)
        self.saldo += valor_deposito + rendimento



