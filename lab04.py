###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 4 - Controle de Estoque
# Nome: Pedro Arrelaro Ribeiro
# RA: 206587
###################################################
vendas=0
estoque=0

while True:
    entrada=int(input())
    estoque=estoque+entrada
    
    if estoque<0:
        print('Quantidade indisponível para a venda de', (-1)*entrada, 'unidades.')
        estoque=estoque-entrada
    else:
        if entrada<0:
            vendas=vendas+1

    if entrada==0:
        break

print('Quantidade de vendas realizadas:', vendas)
print('Quantidade em estoque:', estoque)
    
