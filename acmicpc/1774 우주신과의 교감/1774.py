import sys
input =sys.stdin.readline
N,M = map(int,input().split())
parent = [i for i in range(N+1)]
def getParent(x):
    if x==parent[x]:
        return x
    parent[x] = getParent(parent[x])
    return parent[x]
def unionParent(a,b):
    a=getParent(a)
    b=getParent(b)
    if a<b:parent[b]=a
    else:parent[a]=b
arr = [list(map(int,input().split())) for _ in range(N)]#좌표
query = list()

for i in range(M):
    a,b = map(int,input().split())
    a = getParent(a)
    b = getParent(b)
    if a==b:continue
    unionParent(a,b)

for i in range(N):
    for j in range(i+1,N):
        if getParent(i+1)==getParent(j+1):continue
        d=(abs(arr[i][0]-arr[j][0])**2+abs(arr[i][1]-arr[j][1])**2)**0.5
        # d=abs(arr[i][0]-arr[j][0])+abs(arr[i][1]-arr[j][1])
        query.append([i+1,j+1,d])

query = sorted(query,key=lambda x:x[2])
answer=0
for i in range(len(query)):
    f,t,d = query[i]
    f = getParent(f)
    t = getParent(t)
    if f==t:continue
    unionParent(f,t)    
    answer+=d
print('%.2f' %answer)