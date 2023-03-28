d={}
while True:
  e=input().split(" : ")
  if e[0] == "FIM":
    break
    
  a0=e[0]
  a1=e[1]

  if not a0 in d and int(a1)>0:
    d[a0]=(0,0,0)

  if not a0 in d and int(a1)<0:
    print("Quantidade indisponivel para a venda de",-int(a1), "unidade(s) do produto",e[0]+".")

  
  if a0 in d:
    if int(a1)>0:
      d[a0]=(int(d[a0][0])+int(a1), int(d[a0][1])+1, int(d[a0][2]))
  
    if int(a1)<0 and int(d[a0][0])+int(a1)<0:
      print("Quantidade indisponivel para a venda de",-int(a1), "unidade(s) do produto",e[0]+".")
    if int(a1)<0 and int(d[a0][0])+int(a1)>=0:
      d[a0]=(int(d[a0][0])+int(a1), int(d[a0][1]), int(d[a0][2])+1)

for i in range(len(d)):
  print("Produto:", min(d.keys()))
  print("Quantidade em Estoque:", d[min(d.keys())][0])
  print("Pedidos de Compra:", d[min(d.keys())][1])
  print("Pedidos de Venda:", d[min(d.keys())][2])
  lixo=d.pop(min(d.keys()))