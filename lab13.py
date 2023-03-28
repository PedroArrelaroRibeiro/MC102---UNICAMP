candidatos={}
branco_e_nulo={"Brancos":0,"Nulos":0}

while True:
    entrada=str(input())
    if entrada=="0":
        break
    if entrada=="Branco":
        branco_e_nulo["Brancos"]+=1 
    elif entrada=="Nulo":
        branco_e_nulo["Nulos"]+=1
    
    if entrada!="Branco" and entrada!="Nulo":
        if entrada not in candidatos:
            candidatos[entrada]=[0,entrada]
        candidatos[entrada][0]+=1   



for i in range(len(candidatos)):
    print(max(candidatos.values())[1],max(candidatos.values())[0])
    lixo=candidatos.pop(max(candidatos.values())[1])

print("Brancos",branco_e_nulo["Brancos"])
print("Nulos",branco_e_nulo["Nulos"])