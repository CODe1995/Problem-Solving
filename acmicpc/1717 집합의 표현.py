##########################################################
import sys
input = sys.stdin.readline
def ip():return input().rstrip()
def lip():return list(input().rstrip())
def ii():return int(input())
def mii():return map(int,input().rstrip().split())
def lmii():return list(map(int,input().rstrip().split()))
##########################################################
sys.setrecursionlimit(10**7)
n,m = mii()
parent = [i for i in range(n+1)]
def getParent(z):
    if parent[z]==z:return z
    parent[z] = getParent(parent[z])
    return parent[z]

def unionParent(x,y):
    x = getParent(x)
    y = getParent(y)    
    if x<y:parent[y]=x
    else: parent[x]=y

def findParent(x,y):
    x=getParent(x)
    y=getParent(y)
    if x==y:return 1
    return 0

for _ in range(m):
    c,a,b = mii()
    if c:#1:같은집합인가?
        if findParent(a,b)==1:print('YES')
        else:print('NO')
    else:#집합을 합친다
        unionParent(a,b)
        # print('union',parent)