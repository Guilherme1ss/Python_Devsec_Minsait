from conta import Conta
from datetime import timedelta

class ContaPoupanca(Conta):
    def __init__(self, id_conta: int, saldo: float, taxa_juros_anual: float):
        super().__init__(id_conta, saldo)
        self.taxa_juros_anual = taxa_juros_anual

    def sacar(self, valor: float):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")

    def depositar(self, valor: float, segundos: int = 0, minutos: int = 0, horas: int = 0, dias: int = 0, meses: int = 0, anos: int = 0):
        media_dias_em_mes = 365/12
        total_dias = dias + meses*media_dias_em_mes + anos*365
        tempo_deposito = timedelta(seconds=segundos, minutes=minutos, hours=horas, days=total_dias)
        rendimento = self.calcular_rendimento(tempo_deposito.total_seconds(), valor)
        self.saldo += valor + rendimento

    def calcular_rendimento(self, tempo_deposito: int, valor_deposito: float):
        anos = tempo_deposito / (365 * 24 * 60 * 60)
        taxa_juros_anual = self.taxa_juros_anual / 100
        rendimento = valor_deposito * ((1 + taxa_juros_anual) ** anos - 1)
        return rendimento



