##################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 5 - Jornada de Trabalho
# Nome: Pedro Arrelaro Ribeiro
# RA: 206587
##################################################

V=int(input())
D=int(input())
d=0
horas_por_dia=[]
horas_extras_lista=[]
while d!=D:
  d=d+1
  T=int(input())
  t=0
  x=0
  while t!=T:
    t=t+1
    hi=int(input())
    hf=int(input())
    dh=hf-hi
    x=x+dh
    if t==T:
      horas_por_dia.append(x)

horas_trabalhadas=sum(horas_por_dia)

for i in range(len(horas_por_dia)):
  if horas_por_dia[i]>8:
    horas_extras_lista.append(horas_por_dia[i]-8)

horas_extras=sum(horas_extras_lista)
horas_trabalhadas=sum(horas_por_dia)

if horas_trabalhadas-horas_extras<=44:
  valor=(horas_trabalhadas*V)+(horas_extras*V/2)
else:
  valor=(horas_trabalhadas*V)+(horas_extras*V/2)+((horas_trabalhadas-horas_extras-44)*V/2)
  horas_extras=horas_trabalhadas-44
print("Horas trabalhadas:", horas_trabalhadas)
print("Horas extras:", horas_extras)
print("Valor devido: R$ {:0.2f}".format(valor))