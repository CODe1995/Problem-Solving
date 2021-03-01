import sys
from collections import deque
N,M = map(int,input().split())
field = [list(map(int,list(input().strip()))) for _ in range(N)]
wallList = list()   #벽 좌표
zeroList = list()   #방 좌표
zm = dict() #몇 번 방인지 갯수는 몇 개인지
direction = [[0,1],[1,0],[0,-1],[-1,0]]
def bfs(x,y):
    cnt = 1 #방갯수
    dq = deque([[x,y]])
    while dq:
        x,y = dq.popleft()
        for dx,dy in direction:
            nx = x+dx
            ny = y+dy
            if nx<0 or ny<0 or nx>=M or ny>=N or field[ny][nx]==1 or visited[ny][nx]>0:continue#범위밖,벽
            dq.append([nx,ny])
            visited[ny][nx]=roomNum
            cnt+=1
    return cnt

roomNum = 1
visited = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if field[i][j]==1:wallList.append([j,i])
        else:#방이 나온다?
            if visited[i][j]:continue            
            visited[i][j]=roomNum
            zm[roomNum]=bfs(j,i)#방문안했다면 방의 갯수 파악
            roomNum+=1#방 번호 증가

answer = [[0]*M for _ in range(N)]
for wx,wy in wallList:#벽들 순회
    curRoom = 1#총 방 갯수
    visitRoom = dict()#방문한 방 번호를 저장
    for dx,dy in direction:
        nx = wx+dx
        ny = wy+dy
        if nx<0 or ny<0 or nx>=M or ny>=N or field[ny][nx]==1:continue#범위밖
        if visitRoom and visited[ny][nx] in visitRoom:continue#해당 방을 이미 방문했다면
        visitRoom[visited[ny][nx]]=1#방문한 방 번호 저장
        curRoom+=zm[visited[ny][nx]]#해당 방번호의 방갯수를 저장
    answer[wy][wx]=curRoom%10
    
# for c in visited:
#     print(c)
# print('=====')
for cc in answer:
    for c in cc:
        print(c,end='')
    print()