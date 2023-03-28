###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 12 - Redimensionamento de Imagens
# Nome: Pedro Arrelaro Ribeiro
# RA: 206587
###################################################

def imprimir_imagem(imagem):
    print("P2")
    print(len(imagem[0]), len(imagem))
    print("255")
    for i in range(len(imagem)):
        print(" ".join(str(int(x)) for x in imagem[i]))

def expansao(imagem_original):
    a=2*m-1 # a = colunas
    b=2*n-1 # b = linhas
    
    imagem=[["#" for i in range(a)] for i in range(b)]
    
    
    
    for i in range(n):
        for j in range(m):
            if 0<=i and i<=n:
                if 0<=j and j<=m:
                    imagem[i*2][j*2]=imagem_original[i][j]
               
             
         
    for i in range(b):
        for j in range(a):
            if i%2!=0:
                if j%2==0:
                    imagem[i][j]=(imagem[i+1][j]+imagem[i-1][j])/2
            
    for i in range(b):
        for j in range(a):
            if i%2==0:
                if j%2!=0:
                    imagem[i][j]=(imagem[i][j+1]+imagem[i][j-1])/2
    
    for i in range(b):
        for j in range(a):
            if i%2!=0:
                if j%2!=0:
                    imagem[i][j]=(imagem[i-1][j-1]+imagem[i-1][j+1]+imagem[i+1][j-1]+imagem[i+1][j+1])/4
 
    return imagem
 
def retracao(imagem_original):
    if m%2==0 and n%2==0:
        imagem=[["#" for i in range(int(m/2))] for i in range(int((n/2)))]
    elif m%2!=0 and n%2==0:
        imagem=[["#" for i in range(int((m+1)/2))] for i in range(int((n/2)))]
        for i in range(n):
            imagem_original[i].append(imagem_original[i][m-1])
    elif m%2==0 and n%2!=0:
        imagem=[["#" for i in range(int(m/2))] for i in range(int(((n+1)/2)))]
        imagem_original.append(imagem_original[n-1])
    elif m%2!=0 and n%2!=0:
        imagem=[["%" for i in range(int((m+1)/2))] for i in range(int(((n+1)/2)))]
        for i in range(n):
            imagem_original[i].append(imagem_original[i][m-1])
        imagem_original.append(imagem_original[n-1])
    
    a=len(imagem) #linhas
    b=len(imagem[0]) #colunas
    
    
    while True:
        cta=0
        ctb=0
        for i in range(a):
            for j in range(b):
                imagem[i][j]=(imagem_original[i+cta][j+ctb]+imagem_original[i+cta][j+ctb+1]+imagem_original[i+cta+1][j+ctb]+imagem_original[i+cta+1][j+ctb+1])/4
                ctb=ctb+1
            cta=cta+1
            ctb=0
        break   
    
    return imagem

# leitura da imagem
_ = input() #P2 - linha a ser ignorada

m, n = [int(x) for x in input().split()]
m=int(m) #coluna
n=int(n) #linha

_ = input() #255 - linha a ser ignorada

imagem_original = []
for i in range(n):
    linha = [int(x) for x in input().split()]
    imagem_original.append(linha)

# leitura do tipo de redimensionamento
redimensionamento = str(input())
if redimensionamento == "expansao":
  imagem=expansao(imagem_original)

if redimensionamento == "retracao":
  imagem=retracao(imagem_original)

# impressão da imagem final
imprimir_imagem(imagem)