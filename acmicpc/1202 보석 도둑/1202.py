import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
field = [list(input().strip()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
roomNumber = 0
roomSide = dict() #각 방의 외곽 좌표들을 저장
# O(max) : 1500 * 1500 = 2250000
def bfs(x, y):
  global roomNumber
  dq = deque()
  dq.append([x,y])
  roomNumber+=1 #새로운 영역의 시작이므로 방번호 증가
  while dq:
    # print(dq)
    x, y = dq.popleft()
    for dx, dy in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
      nx, ny = dx + x, dy + y
      if 0 > nx or 0 > ny or M <= nx or N <= ny:continue  #필드밖 안쓰이는 좌표
      if field[ny][nx] == 'X':#벽을 만난 외곽좌표들
        if roomSide and roomNumber in roomSide and [x,y] not in roomSide[roomNumber]:
          roomSide[roomNumber].append([x,y])
        if roomNumber not in roomSide:
          roomSide[roomNumber] = [[x,y]]
        continue
      if visited[ny][nx]>0:continue#이미 방문한 곳
      #탐색하면서 방번호 매기기
      visited[ny][nx]=roomNumber
      dq.append([nx,ny])
target = list()
for i in range(N):
  for j in range(M):
    if field[i][j]=='L':
      target.append(roomNumber+1)#백조가 소속된 방의 번호
      field[i][j]='.'#이동 가능한 필드로 교체
    if field[i][j]=='.' and visited[i][j]==0:
      bfs(j,i)
      
parent = [-1]*roomNumber

def getParent(x):
  if parent[x]==-1:parent[x]=x#초기화
  if x == parent[x]:return x
  parent[x] = getParent(parent[x])
  return parent[x]

def unionParent(a,b):
  a = getParent(a)
  b = getParent(b)
  if a<b:parent[b]=a
  else: parent[a]=b

t = 0
while True:
  for room in roomSide:#방 번호대로 얼음을 녹여줌
    for side in room:#가장자리 좌표를 하나씩 탐색하면서 녹여줌
      

print('---------')
for c in visited:
  print(c)
for c in roomSide:
  print(roomSide[c])