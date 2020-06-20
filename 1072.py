import sys,math
input = sys.stdin.readline

x,y= map(int,input().split())
if y==0:
    print(-1)
else:    
    t = math.trunc(y/x * 100)
    cnt = 0
    while t==math.trunc(y/x*100):
        x+=1
        y+=1
        cnt+=1
    print(cnt)