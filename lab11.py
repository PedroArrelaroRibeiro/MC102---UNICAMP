# Leitura do tabuleiro
T = int(input())
tabuleiro = []
for _ in range(T):
  tabuleiro.append(input().split())

# Leitura da peça
P = int(input())
peca0 = []
for _ in range(P):
  peca0.append(input().split())

# Rodar peças
l0=(len(peca0))
for linha in peca0:
    c0=len(linha)
    break
peca1=[['$' for i in range(l0)] for j in range(c0)]
for a in range(l0): 
  for b in range(c0):
    peca1[b][l0-1-a]=peca0[a][b]

l1=(len(peca1))
for linha in peca1:
    c1=len(linha)
    break
peca2=[['$' for i in range(l1)] for j in range(c1)]
for a in range(l1): 
  for b in range(c1):
    peca2[b][l1-1-a]=peca1[a][b]
     
l2=(len(peca2))
for linha in peca2:
    c2=len(linha)
    break
peca3=[['$' for i in range(l2)] for j in range(c2)]
for a in range(l2): 
  for b in range(c2):
    peca3[b][l2-1-a]=peca2[a][b]

l3=(len(peca3))
for linha in peca3:
  c3=len(linha)
  break
    
# Constantes necessárias para a leitura dos encaixes
e_peca0=0
n_e_peca0=0
x_peca0=0
e_peca1=0
n_e_peca1=0
x_peca1=0
e_peca2=0 
n_e_peca2=0
x_peca2=0
e_peca3=0
n_e_peca3=0
x_peca3=0

# Contagem dos "X"s de cada peça

for linha in peca0:
    a_0=linha.count('X')
    x_peca0=x_peca0+a_0

for linha in peca1:
    a_1=linha.count('X')
    x_peca1=x_peca1+a_1
    
for linha in peca2:
    a_2=linha.count('X')
    x_peca2=x_peca2+a_2
    
for linha in peca3:
    a_3=linha.count('X')
    x_peca3=x_peca3+a_3        

lt=len(tabuleiro)
for linha in tabuleiro:
    ct=(len(linha))
    break

# Leitura dos encaixes

for z0 in range(lt): 
    if z0<=lt-l0:
        for z1 in range(ct): 
            if z1<=ct-c0: 
                for z2 in range(l0): 
                    for z3 in range(c0): 
                        if peca0[z2][z3]=="X" and tabuleiro[z0+z2][z1+z3]==".":
                            n_e_peca0+=1
            if n_e_peca0==x_peca0:
                e_peca0+=1
            n_e_peca0=0       
            
for z0_1 in range(lt): 
    if z0_1<=lt-l1:
        for z1_1 in range(ct): 
            if z1_1<=ct-c1: 
                for z2_1 in range(l1): 
                    for z3_1 in range(c1): 
                        if peca1[z2_1][z3_1]=="X" and tabuleiro[z0_1+z2_1][z1_1+z3_1]==".":
                            n_e_peca1+=1
            if n_e_peca1==x_peca1:
                e_peca1+=1
            n_e_peca1=0

for z0_2 in range(lt): 
    if z0_2<=lt-l2:
        for z1_2 in range(ct): 
            if z1_2<=ct-c2: 
                for z2_2 in range(l2): 
                    for z3_2 in range(c2): 
                        if peca2[z2_2][z3_2]=="X" and tabuleiro[z0_2+z2_2][z1_2+z3_2]==".":
                            n_e_peca2+=1
            if n_e_peca2==x_peca2:
                e_peca2+=1
            n_e_peca2=0
            
for z0_3 in range(lt): 
    if z0_3<=lt-l3:
        for z1_3 in range(ct): 
            if z1_3<=ct-c3: 
                for z2_3 in range(l3): 
                    for z3_3 in range(c3): 
                        if peca3[z2_3][z3_3]=="X" and tabuleiro[z0_3+z2_3][z1_3+z3_3]==".":
                            n_e_peca3+=1
            if n_e_peca3==x_peca3:
                e_peca3+=1
            n_e_peca3=0

# Saída

print('{e0},{e1},{e2},{e3}'.format(e0=e_peca0, e1=e_peca1, e2=e_peca2, e3=e_peca3))
    