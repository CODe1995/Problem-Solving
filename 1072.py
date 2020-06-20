import sys,math
input = sys.stdin.readline

x,y= map(int,input().split())
t = math.trunc(y/x * 100)
bl = 1000000000-x
if y==0 or t==math.trunc((y+bl)/(x+bl)*100):
    print(-1)
else:    
    cnt = 0
    while t==math.trunc(y/x*100):
        x+=1
        y+=1
        cnt+=1
    print(cnt)