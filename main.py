from fabrica_fila import FabricaFila
# from fila_normal import FilaNormal
# from fila_prioritaria import FilaPrioritaria
from constantes import FILA_NORMAL, FILA_PRIORITARIO


fn = FabricaFila.pegar_fila(FILA_NORMAL)
fp = FabricaFila.pegar_fila(FILA_PRIORITARIO)
fn.atualiza_fila()
fn.atualiza_fila()
fn.atualiza_fila()
fn.atualiza_fila()
fp.atualiza_fila()
fn.atualiza_fila()
fn.chama_cliente(5)


# from estatistica import Estatisticas

# from fila_normal import FilaNormal
# from fila_prioritaria import FilaPrioritaria

# fn = FilaNormal()
# fp = FilaPrioritaria()

# dia = "18/10/2021"
# agencia = 203
# flag = "detail"

# fn.atualiza_fila()
# fn.atualiza_fila()
# fn.atualiza_fila()
# fp.atualiza_fila()

# print()
# fn.chama_cliente(5)
# fp.chama_cliente(2)

# print()
# fp.atualiza_fila()
# fn.atualiza_fila()
# fn.atualiza_fila()

# fp.chama_cliente(5)
# fn.chama_cliente(2)
# fn.chama_cliente(3)
# fn.chama_cliente(7)
# fn.chama_cliente(2)
# print()
# estat = Estatisticas.estatistica(fp.clientes_atendidos, dia, agencia, flag)
# print("======================================================================")
# print(f"Data: {estat['data']}")
# print(f"Agência: {estat['agencia']}")
# print(f"Clientes Atendidos: {estat['clientes_atendidos']}")
# print(f"Quantidade de Clientes Atendidos: {estat['qtde_clientes_atendidos']}")
# print("======================================================================")
