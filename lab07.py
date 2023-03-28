#Leitura Listas Ataque*Defesa
lista_defesa=[]
lista_ataque=[]
defesa=int(input())
cte=0
while True:
    tropa_defesa=int(input())
    lista_defesa.append(tropa_defesa)
    cte=cte+1
    if cte==defesa:
        cte=0
        break
ataque=int(input())
while True:
    tropa_ataque=int(input())
    lista_ataque.append(tropa_ataque)
    cte=cte+1
    if cte==ataque:
        cte=0
        break

#Processamento Batalhas
j=-1
while True:
    j=j+1
    vit=0
    der=0
    for i in range(len(lista_ataque)):
        if lista_defesa[i+j]<lista_ataque[i]:
            vit=vit+1
        if lista_defesa[i+j]>lista_ataque[i]:
            der=der+1
    if vit>der:
        print('Vitória posicionando as tropas a partir da posição', j+1)
        break
    if j==len(lista_defesa)-len(lista_ataque):
        print('Derrota')
        break
    
