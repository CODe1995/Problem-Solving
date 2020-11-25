N,M = map(int,input().split())  #가로 N 세로 M
field = []
visited=[[0]*N for _ in range(M)]
move=[(0,1),(1,0),(-1,0),(0,-1)]
sumFoes = 0 #적군의 합
sumAllies = 0 #아군의 합
cnt=0
for _ in range(M):
    field.append(list(map(str,input())))

def bfs(h,w,who):    
    global cnt
    visited[h][w]=1
    for (dx,dy) in move:#다음 방문지 선정
        if w+dx >= 0 and w+dx <N and h+dy>=0 and h+dy<M:
            if visited[h+dy][w+dx]==0 and field[h+dy][w+dx]==who:
                bfs(h+dy,w+dx,who)
    cnt+=1

for h in range(M):#M은세로
    for w in range(N):#N은가로
        if visited[h][w]==1:
            continue
        bfs(h,w,field[h][w])
        res= cnt
        if field[h][w]=='W':
            sumAllies+=res**2
        else:
            sumFoes+=res**2
        cnt=0

print(sumAllies,sumFoes)
