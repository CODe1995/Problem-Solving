import sys
input = sys.stdin.readline
N,M,y,x,K = map(int,input().split())
field = [list(map(int,input().strip().split())) for _ in range(N)]
order = list(map(int,input().strip().split()))
dice = [0,0,0,0,0,0,0]
direction = [[],[1,0],[-1,0],[0,-1],[0,1]]
def diceRoll(num):
    if num==1:#동쪽
        a,b,c,d,e,f = 3,2,6,1,5,4
    elif num==2:#서쪽
        a,b,c,d,e,f = 4,2,1,6,5,3
    elif num==3:#북쪽
        a,b,c,d,e,f = 2,6,3,4,1,5
    elif num==4:#남쪽
        a,b,c,d,e,f = 5,1,3,4,6,2
    dice[1],dice[2],dice[3],dice[4],dice[5],dice[6] = dice[a],dice[b],dice[c],dice[d],dice[e],dice[f]

for o in order:
    nx,ny = x+direction[o][0], y+direction[o][1]
    if nx>=M or 0>nx or 0>ny or ny>=N:continue#명령무시    
    diceRoll(o)
    if field[ny][nx]==0:
        field[ny][nx]=dice[1]#주사위면 -> 지도
    else:
        dice[1]=field[ny][nx]#지도->주사위면
        field[ny][nx]=0#지도는 초기화
    print(dice[6])
    x=nx
    y=ny