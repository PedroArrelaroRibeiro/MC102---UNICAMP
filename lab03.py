###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - Ingresso do Cinema
# Nome: Pedro Arrelaro Ribeiro
# RA: 206587
###################################################

#leitura de dados:

d=int(input()) #dia da semana
h=int(input()) #hora
m=int(input()) #minuto
e=str(input()) #estudante (paga meia sem descunto acumulativo)
p=str(input()) #pagamento 

#dias:

if d==1:
    x=30
    
if d==2 or d==3:
    if h<18:
        x=15
    elif h==18 and m<30:
        x=15
    else:
        x=20
        
if d==4:
    if h<18:
        x=15
    elif h==18 and m<30:
        x=15
    else:
        x=30
        
if d==5:
    if h<18:
        x=20
    elif h==18 and m<30:
        x=20
    else:
        x=30
        
if d==6:
    if h<18:
        x=20
    elif h==18 and m<30:
        x=20
    else:
        x=40
        
if d==7:
    if h<18:
        x=30
    elif h==18 and m<30:
        x=30
    else:
        x=40
    
#estudante

if e=="S":
    x=x/2
  
#cartao  
    
if e=="N" and p=="C":
    if d==1:
        x=x*0.7
    elif d==2 or d==3 or d==4 or d==5:
        x=x*0.5
    elif d==6:
        if h<18:
            x=x*0.5
        elif h==18 and m<30:
            x=x*0.5
        else:
            x=x*0.7
    elif d==7:
        x=x*0.8
 
 #resultado
        
print('Valor do ingresso: R$', format(x, '.2f').replace('.', ','))




















