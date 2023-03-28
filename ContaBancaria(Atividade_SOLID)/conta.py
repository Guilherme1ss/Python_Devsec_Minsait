from abc import ABC, abstractmethod



class Conta(ABC):
    def __init__(self, id_conta: int, saldo: float):
        self.id_conta = id_conta
        self._saldo = saldo
    
    @property
    def saldo(self) -> float:
        return self._saldo
    
    @saldo.setter
    def saldo(self, value: float):
        self._saldo = value
    
    @abstractmethod
    def sacar(self, valor: float) -> bool:
        pass
    
    @abstractmethod
    def depositar(self, valor: float) -> None:
        pass
