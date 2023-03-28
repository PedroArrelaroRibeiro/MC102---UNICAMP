###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 8 - Wordle
# Nome: Pedro Arrelaro Ribeiro
# RA: 206587
###################################################

palavra = str(input())
segredo=[]
for i in palavra:
    segredo.append(i)
print(segredo)
cte=0
while cte!=len(segredo):
    saida=''
    teste=[]
    tentativa=str(input())
    if tentativa==palavra:
        print('Resposta correta')
        break
    for i in tentativa:
        teste.append(i)
    
    for i in range(len(tentativa)):
        if not teste[i] in segredo:
            saida=saida+'_'
        if teste[i] in segredo:
            if teste[i]!=segredo[i]:
                saida=saida+teste[i]
            else:
                saida=saida+teste[i].upper()
    print(saida)
    cte=cte+1
    if cte==len(segredo):
        print('Palavra correta:', palavra)
            
        
    