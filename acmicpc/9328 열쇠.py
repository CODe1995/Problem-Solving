##########################################################
import sys
from collections import deque
direction = [[0,1],[-1,0],[1,0],[0,-1]] #for BFS
input = sys.stdin.readline
def ip():return input().rstrip()
def lip():return list(ip())
def ips():return ip().split()
def ii():return int(input())
def mii():return map(int,ips())
def lmii():return list(mii())
##########################################################
# 말도 안되는 생각을 해보았다..
# visited = [[[0]*(1<<26) for _ in range(100)] for _ in range(100)]

for _ in range(ii()):    
    h,w = mii()
    alpha_door = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alpha_key = 'abcdefghijklmnopqrstuvwxyz'
    docuCnt = 0
    field =  list()
    field.append(list('.'*(w+2)))#윗면 채우기
    doorPosition = [[] for _ in range(26)]#문의 최대 수만큼
    for i in range(h):
        tmp = lip()
        for j in range(w):#문의 위치를 알파벳별로 미리 파악해둔다.
            if tmp[j] in alpha_door:
                doorPosition[ord(tmp[j])-65].append([j+1,i+1])
            elif tmp[j]=='$':#문서의 수를 미리 세두고 다 찾으면 빨리 끝내자.
                docuCnt+=1
        field.append(list('.')+tmp+list('.')) 
    field.append(list('.'*(w+2)))#아랫면 채우기

    def openDoor(key):#키를 전달하면 해당되는 모든 문을 열어주는 함수        
        for dopX,dopY in doorPosition[ord(key)-97]:
            field[dopY][dopX]='.'

    keyarr = lip()    #소유한 키의 상태를 저장한다.    
    if keyarr[0]=='0':
        keyarr=list()#소유한 키가 없는 경우는 넘어간다.
    else:
        for k in keyarr:
            openDoor(k)#이미 획득한 키는 문을 미리 열어둔다.

    answer =0
    def bfs():
        global answer
        visited = [[0]*(w+2) for _ in range(h+2)]
        visited[0][0]=1
        q = deque([[0,0]])
        while q:
            x,y = q.popleft()
            for dx,dy in direction:
                nx,ny = x+dx,y+dy
                if 0<=nx<w+2 and 0<=ny<h+2 and visited[ny][nx]==0:
                    fyx = field[ny][nx]
                    if fyx=='.':
                        visited[ny][nx]=1
                        q.append([nx,ny])
                    elif fyx=='$':
                        answer+=1
                        if docuCnt==answer:
                            return
                        field[ny][nx]='.'
                        visited[ny][nx]=1
                        q.append([nx,ny])
                    elif fyx in alpha_key:#키를 만나면
                        field[ny][nx]='.'
                        q.append([nx,ny])
                        if fyx not in keyarr:
                            keyarr.append(fyx)
                            openDoor(fyx)#해당되는 문열고
                            #visited 리셋
                            visited = [[0]*(w+2) for _ in range(h+2)]
                            visited[ny][nx]=1
                            q.append([nx,ny])
    bfs()
    print(answer)

                            

