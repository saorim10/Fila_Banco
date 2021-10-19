from fila import Fila
from constantes import NORMAL


class FilaNormal(Fila):

    def gera_senha_atual(self) -> None:
        self.senha_atual = f"{NORMAL}-{self.codigo}"
        print(f'Gerando senha: {self.senha_atual}')
    
    def atualiza_fila(self) -> None:
        self.reseta_fila()
        self.gera_senha_atual()
        self.fila_normal.append(self.senha_atual)

    def chama_cliente(self, caixa: int) -> None:
        cliente_atual = self.fila_normal.pop(0)
        Fila.saidas(self, cliente_atual, caixa)
