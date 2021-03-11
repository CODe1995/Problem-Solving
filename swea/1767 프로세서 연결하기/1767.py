cores = list()
field = list()
answer = 10e9
N = 0
maxcc = 0
direction = [[0,1],[1,0],[-1,0],[0,-1]]

def dfs(depth,wires,cc):#깊이, 전선수, 연결된코어수
    global answer,N,field,cores,maxcc
    if depth==len(cores):
        if maxcc <= cc:
            if maxcc < cc:
                answer = wires#새로 변경
            else:
                answer = min(wires,answer) #낮은걸로 갱신
            maxcc = cc
        return
    if len(cores)-depth + cc < maxcc:return#더 이상 진행해도 갯수 달성 못함
    core = cores[depth] #현재 코어 정보 가져옴

    if core[0]==0 or core[1]==0 or core[0]==N-1 or core[1]==N-1:#둘중 하나라도 벽에 닿아있따면
        dfs(depth+1,wires,cc+1)
        return
    dfs(depth+1,wires,cc)#지금껀 포기한채로 탐색해본다.
    for dx,dy in direction:
        wc = 0
        nx = core[0]+dx
        ny = core[1]+dy
        possible = False #파워가 들어가는가?
        wireinstall = False #전선 설치 여부

        while nx>=0 and ny>=0 and nx<N and ny<N:#전선을 설치 할 수 있는 범위인가?
            if field[ny][nx] == 0: #전선 설치가 가능한가?
                wc+=1
                field[ny][nx]=2 #전선 깔기
                possible = True
                wireinstall = True
            else: #전선 설치가 불가능한가?
                possible = False
                break
            nx+=dx; ny+=dy
        
        if possible:#유효하다면?
            dfs(depth+1,wires+wc,cc+1)
        
        while wireinstall and (nx!=core[0] or ny!=core[1]):#현재 nxny가 원래 좌표와 다르다면 복구시킨다. 
            nx-=dx; ny-=dy 
            if nx>=0 and ny>=0 and nx<N and ny<N and field[ny][nx]==2:
                field[ny][nx] = 0     

def init():
    global N,field,answer,cores,maxcc
    T = int(input())
    for t in range(1,T+1):
        maxcc = 0
        cores = list()
        answer = 10e9
        N = int(input())
        field = [list(map(int,input().strip().split())) for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if field[i][j]==1:
                    cores.append([j,i])#코어 좌표 삽입
        dfs(0,0,0)
        print("#"+str(t),answer)
    return

if __name__ == "__main__":
    init()