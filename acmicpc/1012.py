import sys
from collections import deque
visited = list()
def BFS(field,root):    #visited 반환
    direction = [[1,0],[0,1],[-1,0],[0,-1]]
    n = deque([root])   #다음 방문지        
    while n:
        x,y = n.popleft() #방문한 곳 제거, 좌표 저장
        visited[y][x] = 1
        for dx,dy in direction:
            if y+dy < len(field) and x+dx < len(field[0]):
                # 배추가 심어져있고, 아직 방문 안한경우
                if field[y+dy][x+dx]==1 and visited[y+dy][x+dx]==0:
                    n.append([x+dx,y+dy])  

if __name__ == "__main__":    
    T = int(sys.stdin.readline())
    for _ in range(T):
        stack = []  #배추가 있는 곳 저장        
        M,N,K = map(int,sys.stdin.readline().split())  #가로,세로,배추갯수
        field = [[0]*M for _ in range(N)]
        visited = [[0]*M for _ in range(N)]    #방문한 곳 저장
        for _ in range(K):
            n1,n2 = map(int,sys.stdin.readline().split())
            stack.append([n1,n2])   #배추가 있는 좌표값 저장
            field[n2][n1] = 1
        cnt = 0
        for [x,y] in stack:
            if visited[y][x] == 0:    #방문한 기록 없으면
                BFS(field,[x,y])    #방문
                cnt+=1

        # for i in visited:
        #     print(i)
        print(cnt)