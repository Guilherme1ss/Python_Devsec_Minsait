from banco import Banco
from conta import Conta
from datetime import timedelta
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

class ContaPoupanca(Conta, Banco):
    def __init__(self, id_conta: int, saldo: float, taxa_juros_anual: float, banco: Banco, ):
        super().__init__(id_conta, saldo)
        self.banco = banco
        self.banco.validar_poupanca(conta_id= id_conta)
        self.id_conta = id_conta
        self.contas_corrente = banco.contas_corrente
        self.contas_poupanca = banco.contas_poupanca
        self.taxa_juros_anual = taxa_juros_anual
        self.banco.cadastrar_conta_poupanca(conta= self, tipo= 'Conta Poupanca')
        
    def atualizar_saldo_saque(self, valor:float):
        self.saldo >= valor
        self.saldo -= valor
        self.exibir_saldo(valor= valor)

    def sacar(self,valor: float):
        self.sacar_poupança_corrente(valor= valor, id_poupanca= self.id_conta)

    def exibir_saldo(self):
        print("---------------------------------------------------------------")
        print(f"Saldo atual da conta poupança é: {locale.currency(self.saldo, grouping=True)}")
        print("---------------------------------------------------------------")

    def exibir_rendimento(self, rendimento: float):
        print("---------------------------------------------------------------")
        print(f"Após o período informado você terá {locale.currency(rendimento, grouping=True)} em sua conta")
        print("---------------------------------------------------------------")

    def saldo_insuficiente(self, valor:float) -> None:
        print("---------------------------------------------------------------")
        print(f"Saldo insuficiente.\nNão foi possível realizar o saque de R${valor} da sua conta poupança.\nSeu saldo atual é: {locale.currency(self.saldo, grouping=True)}")
        print("---------------------------------------------------------------")

    def verificar_taxa_de_rendimento_ao_ano(self, segundos: int = 0, minutos: int = 0, horas: int = 0, dias: int = 0, meses: int = 0, anos: int = 0):
        self.calcular_tempo_total(segundos= segundos, minutos= minutos, horas= horas, dias= dias, meses= meses, anos= anos)
        rendimento = self.calcular_rendimento(tempo_deposito= self.tempo_deposito.total_seconds(), valor_para_calculo= self.saldo)
        rendimento_total = self.saldo + rendimento
        self.exibir_rendimento(rendimento= rendimento_total)
        
        
    def depositar (self, valor: float):
        self.saldo += valor
        self.exibir_saldo()

    def calcular_tempo_total(self, segundos, minutos, horas, dias, meses, anos):
        self.media_dias_em_mes = 365/12
        self.total_dias = dias + meses*self.media_dias_em_mes + anos*365
        self.tempo_deposito = timedelta(seconds=segundos, minutes=minutos, hours=horas, days=self.total_dias)
        

    def calcular_rendimento(self, tempo_deposito: int, valor_para_calculo: float):
        anos = tempo_deposito / (365 * 24 * 60 * 60)
        taxa_juros_anual = self.taxa_juros_anual / 100
        rendimento = valor_para_calculo * ((1 + taxa_juros_anual) ** anos - 1)
        return rendimento



