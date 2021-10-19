from typing import Dict, Union, List

from fila import Fila


class Estatisticas:
    @staticmethod
    def estatistica(dia: str, agencia: int, flag: str) -> dict:
        # estatistic: Dict[str, Union[List[str], str, int]] = {}

        if flag != "detail":
            estatistic = {f'{agencia}-{dia}': len(Fila.clientes_atendidos)}
        else:
            estatistic = (
                {"data": dia, "agencia": agencia,
                    "clientes_atendidos": Fila.clientes_atendidos,
                    "qtde_clientes_atendidos": len(Fila.clientes_atendidos)})

        return estatistic
