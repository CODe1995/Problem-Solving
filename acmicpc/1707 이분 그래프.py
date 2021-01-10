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
k = ii()   
for _ in range(k):
    v,e = mii()
    graph = [[] for _ in range(v+1)]
    color = [[] for _ in range(v+1)]#색깔을 저장 1,2

    for i in range(e):
        a,b = mii()
        graph[a].append(b)
        graph[b].append(a)
        #일단 모든 간선을 다 수집한다.
    answer=1
    exitFlag = False
    for i in range(1,v+1):
        if not answer:break
        if color[i]:continue#이미 색이 부여됐으므로 건너뜀
        color[i]=1#초기 컬러 설정
        q = deque([i])

        while q:
            x = q.popleft()
            c = 3-color[x]#반대되는 색을 넣어줌
            #색이 없ㅅ다면 색을 넣어줌
            for child in graph[x]:
                if not color[child]:#색이 없다면
                    color[child]=c#반대색 넣어줌
                    q.append(child)
                elif color[child]==color[x]:#색이 같다면
                    answer = 0                        
                    break
    print("YES" if answer else "NO")
            