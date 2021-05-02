import sys
from collections import deque
input = sys.stdin.readline
N,M = map(int,input().split())
direction = [[0,0],[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1]]
field = [list(map(int,input().strip().split())) for _ in range(N)]
order = [list(map(int,input().strip().split())) for _ in range(M)]
clouds = [[0,N-1],[1,N-1],[0,N-2],[1,N-2]]

visited = [[-1]*N for _ in range(N)]    #default -1
for i in range(M):
    d,s = order[i]
    for j in range(len(clouds)):
        dx = direction[d][0]*s
        dy = direction[d][1]*s
        cx = clouds[j][0]
        cy = clouds[j][1]
        nx = cx+dx
        ny = cy+dy
        if nx<0:nx = N-((-nx)%N)
        if ny<0:ny = N-((-ny)%N)
        nx %=N
        ny %=N
        clouds[j][0] = nx   #Step1. 구름의 이동
        clouds[j][1] = ny
        field[ny][nx]+=1    #Step2. 물의 양 증가
        visited[ny][nx]=0   #Step5*. 구름이 사라진 곳 기억
    
    for j in range(len(clouds)):#Step4. 물복사버그 마법 시전
        cx = clouds[j][0]
        cy = clouds[j][1]
        for dx,dy in [[-1,-1],[-1,1],[1,-1],[1,1]]:
            nx,ny = cx+dx, cy+dy
            if 0<=nx<N and 0<=ny<N and field[ny][nx]>0:
                visited[cy][cx]+=1  #Step4-1. 물복사 수량을 visited에 기록
    
    for j in range(len(clouds)):
        cx = clouds[j][0]
        cy = clouds[j][1]
        field[cy][cx] += visited[cy][cx]    #Step4. 물복사버그 적용      

    clouds.clear()  #Step3. 구름이 모두 사라진다.

    for i in range(N):  #Step5. 구름 생성
        for j in range(N):
            if visited[i][j]>=0:
                visited[i][j]=-1
                continue
            if field[i][j]>=2:
                clouds.append([j,i])
                field[i][j]-=2
            
answer = 0
for i in range(N):
    answer+=sum(field[i])
print(answer)
    