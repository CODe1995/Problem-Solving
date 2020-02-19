import sys
from math import gcd

def lcm(a,b):
    return a*b//gcd(a,b)

inp = sys.stdin.readline
T=int(inp().rstrip())
flag = True
for i in range(T):
    # M,N,x,y = input().split()
    lists=inp().rstrip().split()
    for j in range(4):
        lists[j]=int(lists[j])
    M = lists[0]
    M = lists[1]
    for j in range(lcm(lists[0],lists[1])):
        # print((int(x)+int(M)*j),'%',int(N),'==',int(y))
        if (lists[2]+lists[0]*j)%lists[1]==lists[3]:
            print(lists[2]+lists[0]*j)
            flag= False
            break
    if flag == True:
        print('-1')
    else:
        flag=True
