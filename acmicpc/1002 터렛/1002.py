import sys,math
input = sys.stdin.readline

t = int(input())
while t:
    t-=1
    x1,y1,r1,x2,y2,r2 = map(int,input().rstrip().split())
    x = x2-x1
    y = y2-y1
    d = math.sqrt(x**2+y**2) #두 원 거리
    if d==0 and r1==r2:ans=-1
    elif d==abs(r1-r2) or r1+r2==d:ans=1
    elif abs(r1-r2)<d<r1+r2:ans = 2
    else:ans=0
    print(ans)