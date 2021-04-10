w,h = map(int,input().split())
x,y = map(int,input().split())
t = int(input())

dx = 1
dy = 1
ttc = t#남은 시간
for i in range(t):
    nx = x+dx; ny = y+dy
    interval = 0
    if dx>0 and dy>0:
        interval = min(w-nx,h-ny)
    

    
    if 0<=nx<=w and 0<=ny<=h:
        x = nx; y = ny
        continue#아무 문제 없음
    #벽에 부딪혔다면    
    while nx<0 or nx>w or ny<0 or ny>h:#범위를 벗어나면 계속 돌림
        if ny < 0 or ny>h:#y초과
            dy= -1 if dy==1 else 1
        if nx < 0 or nx>w:
            dx= -1 if dx==1 else 1
        nx = x + dx; ny = y+dy
    x = nx; y = ny

print(x,y)