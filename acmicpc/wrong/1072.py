import sys,math
input = sys.stdin.readline

x,y= map(int,input().split()) #게임횟수, 이긴게임
t = math.trunc(y/x * 100) #승률
bl = 1000000000-x # 이 부분이 의미가 없음
# x의 입력값이 10억 이하라는 말이지 게임을 진행 했을때 10억을 넘어갈 수도 있음
# 즉, 승률이 변하지 않는 로직을 찾거나

if y==0 or t==math.trunc((y+bl)/(x+bl)*100):
    print(-1)
else:    
    cnt = 0
    # 이 부분에서 x와 y를 1씩 늘릴게 아니라 이분 탐색처럼 크게 늘려야함.
    while t==math.trunc(y/x*100):
        x+=1
        y+=1
        cnt+=1
    print(cnt)