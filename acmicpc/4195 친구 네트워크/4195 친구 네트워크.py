##########################################################
import sys
input = sys.stdin.readline
def ip():return input().rstrip()
def lip():return list(input().rstrip())
def ips():return ip().split()
def ii():return int(input())
def mii():return map(int,input().rstrip().split())
def lmii():return list(map(int,input().rstrip().split()))
##########################################################
f = ii()
for _ in range(f):    
    n = ii()
    parent = dict()
    parentNum= dict()    
    def find(x):
        if parent[x]==x:return x
        parent[x]=find(parent[x])
        return parent[x]
    def union(x,y):
        x = find(x)
        y = find(y)
        if x!=y:
            parent[y]=x
            parentNum[x]+=parentNum[y]
    def findroot(x):#끝까지 따라감
        if parent[x] == x: return x
        return findroot(parent[x])

    for i in range(n):
        a,b = ips()       
        ca,cb = False,False
        if not a in parent:
            parent[a]=a
            parentNum[a]=1
        if not b in parent:
            parent[b]=b
            parentNum[b]=1
        union(a,b)
        print(parentNum[findroot(a)])
        