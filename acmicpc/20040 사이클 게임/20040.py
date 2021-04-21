import sys
input = sys.stdin.readline

N,M = map(int,input().split())
parent = [i for i in range(N)]
cycle = False

def getParent(x):
    if x==parent[x]:
        return x
    parent[x] = getParent(parent[x])
    return parent[x]

def unionParent(a,b):
    a= getParent(a)
    b= getParent(b)
    if a==b:return
    if a<b:parent[b]=a
    else:parent[a]=b

answer = 0
for i in range(M):
    a,b = map(int,input().split())
    if cycle:continue
    if getParent(a)==getParent(b):
        cycle=True
        answer = i+1
    unionParent(a,b)
print(answer)
    