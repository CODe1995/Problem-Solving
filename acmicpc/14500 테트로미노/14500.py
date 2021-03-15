import sys
input = sys.stdin.readline
N,M = map(int,input().split())
field = [list(map(int,input().strip().split())) for _ in range(N)]

etcs = [
    [[1,1,1],[0,1,0]], #ㅜ   
    [[1,0],[1,1],[1,0]],#ㅏ
    [[0,1],[1,1],[0,1]],#ㅓ
    [[0,1,0],[1,1,1]]#ㅗ
]

direction = [[0,1],[1,0],[-1,0],[0,-1]]
answer = 0
visited = [[0]*M for _ in range(N)]
def dfs(depth,x,y,tsum):
    global answer
    if depth==4:
        answer = max(answer,tsum)
        return
    for dx,dy in direction:        
        nx = dx+x
        ny = dy+y
        if 0<=nx<M and 0<=ny<N and visited[ny][nx]==0:#필드밖 체크      
            visited[ny][nx]=1
            dfs(depth+1,nx,ny,tsum+field[ny][nx])
            visited[ny][nx]=0

def checkETC(x,y):
    global answer
    tmax = 0
    tsum = 0
    for etc in etcs:
        tsum=0#도형 전환마다 초기화
        height = len(etc)#세로 수
        for i in range(height):
            for j in range(len(etc[0])):#가로 수
                if etc[i][j]==1 and x+j<M and y+i<N:#유효
                    tsum+=field[y+i][x+j]
        tmax = max(tmax,tsum)
    answer = max(tmax,answer)

for i in range(N):
    for j in range(M):
        visited[i][j]=1
        dfs(1,j,i,field[i][j])
        visited[i][j]=0
        checkETC(j,i)
print(answer)