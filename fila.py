from abc import abstractmethod
from typing import List

from constantes import TAMANHO_PADRAO_MAXIMO, TAMANHO_PADRAO_MINIMO


class Fila:
    codigo: int = 0
    fila: List[str] = []
    fila_normal: List[str] = []
    fila_prioritario: List[str] = []
    clientes_atendidos: List[str] = []
    senha_atual: str = ""

    @abstractmethod
    def gera_senha_atual(self) -> None:
        ...
    
    def reseta_fila(self) -> None:
        if self.codigo >= TAMANHO_PADRAO_MAXIMO:
            self.codigo = TAMANHO_PADRAO_MINIMO
        else:
            self.codigo += 1

    @abstractmethod
    def atualiza_fila(self) -> None:
        ...

    @abstractmethod
    def chama_cliente(self, caixa: int) -> None:
        ...

    def saidas(self, cliente_atual, caixa):
        self.clientes_atendidos.append(cliente_atual)
        print(f"\nCliente: {cliente_atual}, dirija-se ao caixa {caixa}") 
        print(f"Clientes na Fila: {self.fila_prioritario + self.fila_normal}")
        print(f"Clientes Atendidos: {self.clientes_atendidos}")