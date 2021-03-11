from itertools import permutations
import sys
input = sys.stdin.readline
T = int(input())
card = [i for i in range(1,19)]
totalGames = 362880
for t in range(1,T+1):
    myCard = list(map(int,input().strip().split()))
    yourCard = list()
    for i in range(0,18):
        if i+1 not in myCard:
            yourCard.append(i+1)
    perm = permutations(yourCard)
    win=0
    for case in perm:
        myPoint=0
        yourPoint=0
        for i in range(9):
            if case[i]<myCard[i]:
                myPoint += case[i]+myCard[i]
            else:
                yourPoint += case[i]+myCard[i]
        if myPoint>yourPoint:
            win+=1
    # print(win)
    print('#'+str(t),win,(totalGames-win))
