import sys
sys.setrecursionlimit(10000000)
g_grid = []
direction = [[0,-1],[1,0],[0,1],[-1,0]]#북 동 남 서 (우향)
answer = []
#추적 경로
traced = dict()
N,M =0,0
def dfs(x,y,d,depth):
    global answer, g_grid, traced, N, M
    v = x + y*len(g_grid[0])  # 현재 노드의 번호    
    if traced and str(v)+','+str(d) in traced: #순환 발생        
        if depth != 0:
            answer.append(depth)
        return
    
    nd = d
    nx,ny = x,y
    #방향 전환
    if g_grid[y][x] == 'S':
        nx,ny = x+direction[d][0],y+direction[d][1]
    if g_grid[y][x] == 'L':
        nd = d+4-1 if d-1<0 else d-1
        nx,ny = x+direction[nd][0],y+direction[nd][1]
    if g_grid[y][x] == 'R':
        nd = (d+1) % 4
        nx,ny = x+direction[nd][0],y+direction[nd][1]
    nx =  nx+M if nx<0 else nx%M
    ny =  ny+N if ny<0 else ny%N

    traced[str(v)+','+str(d)]=1    
    dfs(nx,ny,nd,depth+1)
    # traced.pop(str(v)+','+str(d))    

    

def solution(grid):
    global g_grid, answer, traced, N, M
    answer=[]
    traced.clear()
    g_grid = grid
    N,M = len(grid), len(grid[0])
    for i in range(N):
        for j in range(M):
            for d in range(4):
                ret = dfs(j,i,d,0)
    
    return sorted(answer) 

# print(solution(["SL","LR"]))
# print(solution(['S']))
# print(solution(['R','R']))
# print(solution(['SLL','LLL','LLL']))
# print(solution(['LL','LL','LL']))
# print(solution(['RRR','LLL','RRR','LLL']))
inputs = [['R','L'],
            ['RRRRR','RRRLL'],
            ['LR','RS'],
            ['SSSSSSSSSSSSSSSSSSSS'],
            ['LL','LL'],
            ['RLR','RLR','RLR'],
            ['LRS','LRS','LRS','LRS','LRS','LRS'],
            ['L'],
            ['R'],
            ['S'],
            ['LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL']]

for ip in inputs:
    print(solution(ip))