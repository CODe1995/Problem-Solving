import sys
from collections import deque
input = sys.stdin.readline
N,M = map(int,input().split())
deck = [deque(),deque()]
ground = [deque(),deque()]
for _ in range(N):
    a,b = map(int,input().split())
    deck[0].appendleft(a)
    deck[1].appendleft(b)
turn = 0
for _ in range(M):#M번 진행
    ground[turn].appendleft(deck[turn].popleft())    
    if not deck[turn]:break
    win = -1
    
    for i in [0,1]:
        if (ground[i] and ground[i][0]==5):win = 0
    if ground[0] and ground[1] and ground[0][0]+ground[1][0]==5:win = 1

    if win!=-1:
        for i in [1-win,win]:
            while ground[i]:
                deck[win].append(ground[i].pop())
    turn = 1-turn

# print(dodq,sudq)
if len(deck[0])>len(deck[1]):winFlag=0
elif len(deck[0])<len(deck[1]):winFlag=1
else:winFlag=2
print(['do','su','dosu'][winFlag])