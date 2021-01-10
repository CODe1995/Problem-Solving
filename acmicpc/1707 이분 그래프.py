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
    color = [[] for _ in range(v+1)]#색깔을 저장
    def bfs():
        for i in range(1,v+1):
            if graph[i]:#그래프가 존재하면                
                if color[i]:#해당 그래프에 색이 있다면
                    for child in graph[i]:
                        if child==i:continue#자기자신은패스
                        if not color[child]:#자식의 색이 없을때
                            color[child]=not color[i]
                        else:#자식의 색이 있다면?
                            if color[child]==color[i]:#서로 색이 같다?
                                return 'NO'
                            else:#다르다
                                continue
                else:#해당 그래프에 색이 없다면
                    #이어지는 정점은 반대 색깔로 칠해준다.
                    color[i]=0
                    for child in graph[i]:
                        if child==i:continue#자기자신은패스
                        if color[child]:#이미 자식정점에 컬러가 있다면
                            if color[child]==color[i]:#색이 겹친다면
                                return 'NO'
                            else:#색이 안겹치면
                                continue
                        else:#자식이 색깔이 없다면?
                            color[child] = not color[i]#반대 색깔을 칠해준다.
        return 'YES'
    for i in range(e):
        a,b = mii()
        graph[a].append(b)
        graph[b].append(a)
        #일단 모든 간선을 다 수집한다.
    
    print(bfs())