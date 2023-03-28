#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 14 - Caminho Binário Alternado
# Nome: Pedro Arrelaro Ribeiro
# RA: 206587
#####################################################
# Funcoes

def fleste(x,y):
  if [x,y+1] not in coordenadas:
    if tabuleiro[x][y]==tabuleiro[x][y+1] and [x,y+1] not in coordenadas:
      coordenadas.append([x,y+1])
      return y
    elif tabuleiro[x][y]!=tabuleiro[x][y+1] and [x,y+1] not in caminhos:
      y=y+1
      if [x,y]==[lf,cf]:
        caminho_encontrado.append("caminho encontrado")
      caminhos.append([x,y])
      return y
    else:
      return y
  else:
    return y 
      
      
def fnorte(x,y):
  if [x-1,y] not in coordenadas:
    if tabuleiro[x][y]==tabuleiro[x-1][y] and [x-1,y] not in coordenadas:
      coordenadas.append([x-1,y])
      return x
    elif tabuleiro[x][y]!=tabuleiro[x-1][y] and [x-1,y] not in caminhos:
      x=x-1
      if [x,y]==[lf,cf]:
        caminho_encontrado.append("caminho encontrado")
      caminhos.append([x,y]) 
      return x
    else:
      return x
  else:
    return x
        
def foeste(x,y):
  if [x,y-1] not in coordenadas:
    if tabuleiro[x][y]==tabuleiro[x][y-1] and [x,y-1] not in coordenadas:
      coordenadas.append([x,y-1])
      return y
    elif tabuleiro[x][y]!=tabuleiro[x][y-1] and [x,y-1] not in caminhos:
      y=y-1
      if [x,y]==[lf,cf]:
        caminho_encontrado.append("caminho encontrado")
      caminhos.append([x,y]) 
      return y
    else:
      return y
  else:
    return y   
   
def fsul(x,y):
  if [x+1,y] not in coordenadas:
    if tabuleiro[x][y]==tabuleiro[x+1][y] and [x+1,y] not in coordenadas:
      coordenadas.append([x+1,y])
      return x
    elif tabuleiro[x][y]!=tabuleiro[x+1][y] and [x+1,y] not in caminhos:
      x=x+1
      if [x,y]==[lf,cf]:
        caminho_encontrado.append("caminho encontrado")
      caminhos.append([x,y]) 
      return x
    else: 
      return x
  else:
    return x

# Leitura dos dados

L = int(input())

tabuleiro = [input().split() for _ in range(L)]



li, ci, lf, cf = [int(i) for i in input().split()]
la=li
ca=ci

coordenadas=[[li,la]]
caminho_encontrado=[]

while True:
  
  coordenadas_inicio=len(coordenadas)
  caminhos=[]
  
  
  while True:
    
    caminhos_inicio=len(caminhos)
    coordenadas_inicio=len(coordenadas)
    
    if la==0 and ca==0:
      ca=fleste(la,ca)
    if la==0 and ca==0:
      la=fsul(la,ca)
    
    if la==0 and ca==len(tabuleiro[0])-1:
      ca=foeste(la,ca)
    if la==0 and ca==len(tabuleiro[0])-1:  
      la=fsul(la,ca) 
    
    if la==len(tabuleiro)-1 and ca==0:
      la=fnorte(la,ca)
    if la==len(tabuleiro)-1 and ca==0:  
      ca=fleste(la,ca)
    
    
    if la==len(tabuleiro)-1 and ca==len(tabuleiro[0])-1:
      la=fnorte(la,ca)
    if la==len(tabuleiro)-1 and ca==len(tabuleiro[0])-1:  
      ca=foeste(la,ca)
    
    
    if la==0 and ca!=0 and ca!=len(tabuleiro[0])-1:
      la=fsul(la,ca)
    if la==0 and ca!=0 and ca!=len(tabuleiro[0])-1:  
      ca=fleste(la,ca)
    if la==0 and ca!=0 and ca!=len(tabuleiro[0])-1:  
      ca=foeste(la,ca)
    
    
    if la!=0 and la!=len(tabuleiro)-1 and ca==0:
      la=fsul(la,ca)
    if la!=0 and la!=len(tabuleiro)-1 and ca==0:  
      la=fnorte(la,ca)
    if la!=0 and la!=len(tabuleiro)-1 and ca==0:  
      ca=fleste(la,ca)
    
    
    if la==len(tabuleiro)-1 and ca!=0 and ca!=len(tabuleiro[0])-1:
      la=fnorte(la,ca)
    if la==len(tabuleiro)-1 and ca!=0 and ca!=len(tabuleiro[0])-1:  
      ca=fleste(la,ca)
    if la==len(tabuleiro)-1 and ca!=0 and ca!=len(tabuleiro[0])-1:  
      ca=foeste(la,ca)
   
    
    if la!=0 and la!=len(tabuleiro)-1 and ca==len(tabuleiro[0])-1:
      la=fnorte(la,ca)
    if la!=0 and la!=len(tabuleiro)-1 and ca==len(tabuleiro[0])-1:  
      la=fsul(la,ca)
    if la!=0 and la!=len(tabuleiro)-1 and ca==len(tabuleiro[0])-1:  
      ca=foeste(la,ca)
    
    
    if la!=0 and la!=len(tabuleiro)-1 and ca!=0 and ca!=len(tabuleiro[0])-1:
      la=fnorte(la,ca)
    if la!=0 and la!=len(tabuleiro)-1 and ca!=0 and ca!=len(tabuleiro[0])-1:  
      la=fsul(la,ca)
    if la!=0 and la!=len(tabuleiro)-1 and ca!=0 and ca!=len(tabuleiro[0])-1:  
      ca=foeste(la,ca)
    if la!=0 and la!=len(tabuleiro)-1 and ca!=0 and ca!=len(tabuleiro[0])-1:  
      ca=fleste(la,ca)
      
    caminhos_fim=len(caminhos)
    if caminhos_inicio==caminhos_fim and [la,ca] not in coordenadas:
      coordenadas.append([la,ca])
      la=li
      ca=ci
      break
    if "caminho encontrado" in caminho_encontrado:
      break
    
    coordenadas_fim=len(coordenadas)
    if caminhos_inicio==caminhos_fim and coordenadas_inicio==coordenadas_fim:
      break
    
  if "caminho encontrado" in caminho_encontrado:
    print("caminho encontrado")
    break  
  
  coordenadas_fim=len(coordenadas)
  
  if coordenadas_inicio==coordenadas_fim:
    print("caminho nao encontrado")
    break
  if [lf,cf] in coordenadas:
    print("caminho nao encontrado")
    break