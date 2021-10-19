from fila import Fila
from constantes import PRIORITARIO


class FilaPrioritaria(Fila):

    def gera_senha_atual(self) -> None:
        self.senha_atual = f"{PRIORITARIO}-{self.codigo}"
        print(f'Gerando senha: {self.senha_atual}')
    
    def atualiza_fila(self) -> None:
        self.reseta_fila()
        self.gera_senha_atual()
        self.fila_prioritario.append(self.senha_atual)

    def chama_cliente(self, caixa: int) -> None:
        cliente_atual = self.fila_prioritario.pop(0)
        Fila.saidas(self, cliente_atual, caixa)
