from typing import Union

from fila_normal import FilaNormal
from fila_prioritaria import FilaPrioritaria
from constantes import FILA_NORMAL, FILA_PRIORITARIO


class FabricaFila:
    @staticmethod
    def pegar_fila(tipo_fila) -> Union[FilaNormal, FilaPrioritaria]:
        if tipo_fila == FILA_NORMAL:
            return FilaNormal()
        elif tipo_fila == FILA_PRIORITARIO:
            return FilaPrioritaria()
        else:
            raise NotImplementedError("Tipo de Fila não Existe")
