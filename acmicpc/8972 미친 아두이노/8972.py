import sys
from collections import deque
jongsu_direction = [[-1,-1],[-1,1],[0,1],[1,1],[-1,0],[0,0],[1,0],[-1,-1],[0,-1],[1,-1]]
direction = [[-1,-1],[-1,1],[0,1],[1,1],[-1,0],[1,0],[-1,-1],[0,-1],[1,-1]]
N,M = map(int,input().split())
field = list()
root = []
enemy = dict()
visited = [[dict()]*M for _ in range(N)]
for i in range(N):
    field.append(list(input().strip()))
    for j in range(M):
        if field[i][j]=='I':
            root = [j,i]
        elif field[i][j] == 'R':
            sz= len(enemy)
            enemy[sz]=[j,i]
            visited[i][j][sz]=1
            # enemy.append([j,i])
order = list(map(int,list(input().strip())))
# print(order)
#종수가 먼저 움직임
rx,ry = root[0],root[1]

def solution():
    global rx,ry,field,order,visited
    for m in range(len(order)):
        #종수차례
        move = order[m]
        dx,dy = jongsu_direction[move]
        nx,ny = rx+dx, ry+dy
        if 0<=nx<M and 0<=ny<N:
            if field[ny][nx]=='R':#아두이노가 있다면? 게임종료
                print('kraj',(m+1))#게임종료
                return
            #이동한다면
            field[ry][rx]='.'#원래 있던 자리 초기화
            field[ny][nx]='I'#이동하는 자리
            rx,ry = nx,ny #좌표교환
        
        #적차례
        delete = list()#겹쳐서 사라지는 적군의 visited 좌표

        for e in enemy:#적군 하나씩 돌아가면서 턴
            ex,ey = enemy[e]
            far = abs(ex-rx)+abs(ey-ry) #종수와 거리값
            n_move = []
            for dx,dy in direction:#8방
                nx,ny = ex+dx, ey+dy
                n_far = abs(nx-rx)+abs(ny-ry) #종수와 거리값
                if 0<=nx<M and 0<=ny<N and n_far<=far:
                    n_move = [nx,ny]#다음 이동할 좌표를 "저장"만 해둠
                    far = n_far#가장 가까운 거리를 갱신
            
            ax,ay = n_move  #다음으로 이동할 좌표
            enemy[e]=[ax,ay]#다음좌표로 갱신
            
            visited[ey][ex]-=1            
            visited[ay][ax]+=1
            if visited[ey][ex]==0:#원래 자리에 아무도 없다면
                field[ey][ex] = '.' #원래 있던곳 초기화            

            if field[ay][ax]=='R':#겹치는 애가 있다?
                if [ax,ay] not in delete:
                    delete.append([ax,ay])#제거목록에 추가

            elif field[ay][ax]=='I':#종수랑 겹침
                print('kraj',(m+1))#게임종료
                return            
            field[ay][ax]='R'
        
        while delete:#겹치는곳 삭제
            delx,dely = delete.pop()
            if len(visited[dely][delx])==1:continue
            for x in visited[dely][delx]:
                del enemy[x]      
            field[dely][delx]='.'#펑~
        # print('==========')
    for c in field:
        for z in c:
            print(z,end='')
        print()
solution()