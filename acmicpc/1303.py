def bfs(field,width,height):
    sumFoes = 0 #적군의 합
    sumAllies = 0 #아군의 합
    visited=[[0]*width for _ in range(height)]
    
    nextq=[]
    nextq.append((0,0))
    move=[(0,1),(1,0),(-1,0),(0,-1)]
    while nextq:
        dx,dy = nextq.pop(0)
        for x,y in move:#다음 방문지 선정
            if dx+x >= 0 and dx+x <width and dy+y>=0 and dy+y<height and visited[dx+x][dy+y]==0:
                nextq.append((dx+x,dy+y))#다음 방문지를 nextq에 넣는다.
        
        
            
        
        
        

N,M = map(int,input().split())  #가로 N 세로 M
field = []
for _ in range(M):
    field.append(list(map(str,input())))

print(bfs(field,N,M))
    