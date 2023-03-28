n = int(input())
matriz = [input().split() for _ in range(n)]
team=str(input())
rounds=int(input())

while_ct1=0
points_team1=0
points_team2=0

while while_ct1 != rounds:
    route=input()
    list_route=[]
    for i in route:
        list_route.append(i)
    
    x=0
    y=0
    
    for i in list_route:
        if i=="N":
            x=x-1
            if matriz[x][y]=="*":
                matriz[x][y]="."
                if while_ct1%2==0:
                    points_team1+=1
                elif while_ct1%2!=0:
                    points_team2+=1
        elif i=="S":
            x=x+1
            if matriz[x][y]=="*":
                matriz[x][y]="."
                if while_ct1%2==0:
                    points_team1+=1
                elif while_ct1%2!=0:
                    points_team2+=1
        elif i=="O":
            y=y-1
            if matriz[x][y]=="*":
                matriz[x][y]="."
                if while_ct1%2==0:
                    points_team1+=1
                elif while_ct1%2!=0:
                    points_team2+=1
        elif i=="L":
            y=y+1
            if matriz[x][y]=="*":
                matriz[x][y]="."
                if while_ct1%2==0:
                    points_team1+=1
                elif while_ct1%2!=0:
                    points_team2+=1
        
                         
    while_ct1=while_ct1+1
  
blue_points=0
red_points=0    
if team=="azul":
    blue_points=points_team1
    red_points=points_team2
if team=="vermelho":
    blue_points=points_team2
    red_points=points_team1
    
print('Tesouros encontrados pelo time azul:', blue_points)
print('Tesouros encontrados pelo time vermelho:', red_points)

if blue_points>red_points:
    print('Vitoria do time azul')
elif red_points>blue_points:
    print('Vitoria do time vermelho')
elif blue_points==red_points:
    print('Empate')
