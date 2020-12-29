##########################################################
import sys
input = sys.stdin.readline
def ip():return input().rstrip()
def lip():return list(input().rstrip())
def ii():return int(input())
def mii():return map(int,input().rstrip().split())
def lmii():return list(map(int,input().rstrip().split()))
##########################################################
# sys.setrecursionlimit(10**7)
n=ii()
m=ii()
parent = [i for i in range(n+1)]
def find(x):
    if parent[x]==x:return x
    parent[x] = find(parent[x])
    return parent[x]
def union(a,b):
    a = find(a)
    b = find(b)
    if a<b:parent[b]=a
    else:parent[a]=b
def check(a,b):
    a=find(a)
    b=find(b)
    if a==b:return 1
    return 0

for i in range(1,n+1):
    tmp = lmii()
    for j in range(1,n+1):
        if tmp[j-1]==1:
            union(i,j)
quest = lmii()
for i in range(1,m):
    if check(quest[i-1],quest[i])==0:
        print('NO')
        sys.exit()
print('YES')
