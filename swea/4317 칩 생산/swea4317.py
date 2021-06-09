import sys,os
# print(os.listdir(os.getcwd()+'\\swea\\4317 칩 생산'))
sys.stdin = open(os.getcwd()+'\\swea\\4317 칩 생산\\sample_input.txt','r')

field = []
CHIP = [[1,1],[1,1]]
N,M = -1,-1
cnt = 0
answer = 0

#칩 설치가 가능한지 확인하는 함수
def checkPossible(x,y):
    global N,M
    if y+1 < N and x+1 < M:#칸을 벗어나지 않고
        if [field[y][x],field[y][x+1],field[y+1][x],field[y+1][x+1]]==[0,0,0,0]:#4칸 모두 비어있다면
            return True
    return False    

def createChip(x,y):
    field[y][x],field[y][x+1],field[y+1][x],field[y+1][x+1]=2,2,2,2

def deleteChip(x,y):
    field[y][x],field[y][x+1],field[y+1][x],field[y+1][x+1]=0,0,0,0

def getMaximumChip(x,y):
    global N,M,answer
    if answer > ((N-1-y)//2)*(M//2)+cnt:
        return False
    return True
    # w = (M-x)//2

#DFS
def dfs(x,y):
    global cnt,answer,field,N,M
    for i in range(y,N):
        
        j = x
        

TC = int(input())
for tc in range(1,TC+1):
    N,M = map(int,input().split())
    field = [list(map(int,input().split())) for _ in range(N)]
    cnt = 0
    answer=0
    dfs(0,0)
    print('#{} {}'.format(tc,answer))