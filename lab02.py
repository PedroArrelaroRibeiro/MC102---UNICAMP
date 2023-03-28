###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 2 - Rumo a Marte
# Nome: Pedro Arrelaro Ribeiro
# RA: 206587
###################################################

# Leitura de dados
D1=int(input())
V1=int(input())
T=int(input())
D2=int(input())
V2=int(input())
# Cálculo do tempo total gasto por cada espaçonave 
t1=D1/V1
t2=24*T+D2/V2
# Impressão da resposta
if t1<t2:
  print(True)
else:
  print(False)