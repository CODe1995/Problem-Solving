#Parallel Binary Search :: PBS
#[ACM] 1396 - 크루스칼의 공
#필요지식 Union-find, Binary Search
MAXARR = 111111
#전역부분
import sys
input = sys.stdin.readline
parent = [-1]*MAXARR

#부모 노드를 찾는 함수
def getParent(a):
    if(parent[a]<0): return a   #첫 값이 -1이라면 자신이 부모임.
    parent[a] = getParent(parent[a])
    return parent[a]

#두 부모 노드를 합치는 함수
def unionParent(a,b):
    a = getParent(a)
    b = getParent(b)
    if a==b: return
    if parent[a] < parent[b]: 
        a,b = b, a #swap(a,b)
    parent[b] += parent[a]
    parent[a] = b

#같은 부모를 가지는지 확인하는 함수
def findParent(a,b):
    a = getParent(a)
    b = getParent(b)
    if a==b: return 1
    return 0

#정점, 간선
vertex, edge = map(int,input().rstrip().split())
graph = [-1]*(edge)
for i in range(1,edge+1):
    a,b,c = map(int,input().rstrip().split())
    graph[i-1]= [c,[a,b]]
# print(graph)
graph.sort(key=lambda x: x[0])
# print('최소 거리로 정렬 :',graph)

#쿼리 입력
q = int(input())
query = [-1]*MAXARR
for i in range(q):
    a,b = map(int,input().rstrip().split())
    query[i]=[a,b]

# 간선 연결
answer = [-1]*MAXARR
treeSize = [-1]*MAXARR
for i in range(edge):
    unionParent(graph[i][1][0],graph[i][1][1])
    # print(parent[:vertex+1])
    for j in range(q):
        if answer[j]==-1 and findParent(query[j][0],query[j][1]):
            answer[j] = i
            treeSize[j] = -parent[getParent(query[j][0])]
#     print(i,'answer :',answer[:vertex+1])
#     print(i, 'treeSize :',treeSize[:vertex+1])
# print('parent :',parent[:7])
# sys.exit()
for i in range(q):
    if answer[i]==-1:#경로가 없을때
        print(-1)
    else:
        print(graph[answer[i]][0],treeSize[i])