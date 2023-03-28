##################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 6 - Torre de Panquecas
# Nome:
# RA:
##################################################

# Leitura da torre de panquecas
torre = [int(panqueca) for panqueca in input().split()]
# Leitura e processamento dos movimentos
while True:
    M=int(input())
    if M==0:
        break
    topo_da_torre = torre[M-1::-1]
    resto_da_torre = torre[M:len(torre)]
    torre = topo_da_torre + resto_da_torre
# Impressão da saída

if torre == sorted(torre):
    print('Torre estavel')
else:
    print('Torre instavel')