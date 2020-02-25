def bfs(field,width,height):
    visited=[]
    visited=[[0]*width for _ in range(height)]
    visited[0][0]=field[0][0]
    next_q = []
    next_q.append((0,0))
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    sumen = 0 #적군합
    sumur = 0 #아군합
    while next_q:
        bx,by = next_q.pop(0)
        for i in range(4):
            ax = bx + dx[i]
            ay = by + dy[i]
            if ax<width and ay<height and ax>=0 and ay>=0 and visited[ax][ay]==0:
                if visited
    return #우리팀 적팀 N^2
N,M = map(int,input().split())  #가로 N 세로 M
field = []
for _ in range(M):
    field.append(list(map(str,input())))

print(bfs(field,N,M))
    