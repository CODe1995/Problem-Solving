import sys
input =sys.stdin.readline

N,M = map(int,input().split())
s,e = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(M)]
arr = sorted(arr,key=lambda x:-x[2])
parent = [i for i in range(N+1)]
def getParent(x):
    if x==parent[x]:
        return x
    parent[x] = getParent(parent[x])
    return parent[x]
def unionParent(a,b):
    a = getParent(a)
    b = getParent(b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b
tmp = 10e9
answer = 10e9
for a,b,k in arr:
    a,b=getParent(a),getParent(b)
    if(a==b):
        continue
    unionParent(a,b)
    tmp = min(tmp,k)
    if(getParent(s)==getParent(e)):
        answer = tmp
        break
print(answer if answer!=10e9 else 0)