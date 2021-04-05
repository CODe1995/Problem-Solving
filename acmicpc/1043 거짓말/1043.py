import sys
input = sys.stdin.readline
N,M = map(int,input().split())
known = list(map(int,input().split()))
parent = [0]+[i for i in range(1,N+1)]
def find(x):
    global parent
    if x == parent[x]: return x
    parent[x] = find(parent[x])
    return parent[x]
def union(a,b):
    a = find(a)
    b= find(b)
    if a<b:parent[b]=a
    else:parent[a]=b

for k in range(1,len(known)):
    x = known[k]
    if find(x)==0:continue
    union(0,x)

answer = 0
party = list()
for i in range(M):
    p = list(map(int,input().split()))
    party.append(p)
    for j in range(2,len(p)):        
        if find(parent[p[j-1]])==find(parent[p[j]]):
            continue
        union(parent[p[j-1]],parent[p[j]])
# print(parent)
for i in range(len(party)):
    target = party[i]
    for j in range(1,len(target)):
        if find(parent[target[j]])==0:break
    else:
        # print("++",target)        
        answer+=1
# print(parent)
print(answer)