import sys
input = sys.stdin.readline

N,M,K = map(int,input().split())    #도시갯수, 케이블, 발전소
parent = [i for i in range(N+1)]
pp = list(map(int,input().split())) #power plant 발전소
arr = []

for i in range(M):    
    a,b,d = map(int,input().split())
    arr.append([a,b,d])
arr = sorted(arr,key=lambda x:x[2]) #가치 오름차순으로 정렬

def find(x):
    if parent[x]==x:return x
    parent[x] = find(parent[x])
    return parent[x]
def union(a,b):
    a = find(a)
    b = find(b)
    if a==b:return False
    app = a in pp
    bpp = b in pp
    if app and bpp:# 둘 다 발전소에 연결되어 있다면
        return False#굳이 연결할 필요 없음    
    if app:#a가 발전소에 연결되어 있다면
        parent[b]=a#발전소 쪽으로 연결        
    elif bpp:
        parent[a]=b        
    else:#둘 다 발전소에 연결되어 있지 않다면?
        if a<b:parent[b] = a
        else:parent[a]=b
    return True

answer = 0
for i in range(len(arr)):
    a,b,d = arr[i]    
    if union(a,b):
        answer+=d
print(answer)