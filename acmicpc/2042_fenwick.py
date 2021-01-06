##########################################################
import sys
input = sys.stdin.readline
def ii():return int(input())
def mii():return map(int,input().rstrip().split())
def lmii():return list(map(int,input().rstrip().split()))
##########################################################
#Fenwick Tree로 구현하기
n,m,k = mii()
node = [0]*(n+1)
tree = [0]*(n+1)

def update(i, dif):
    # print('before:',tree)
    while i <= n:
        tree[i]+=dif
        i+=(i&-i)
    # print('after:',tree)

def sumt(i):
    ans = 0
    while i>0:
        ans+=tree[i]
        i -= (i&-i)
    return ans

for i in range(1,n+1):
    node[i] = ii()
    update(i,node[i])

for _ in range(m+k):
    a,b,c = mii()
    if a==1:
        dif = c-node[b]
        node[b]=c
        update(b,dif)
    else:
        if b>c:b,c=c,b
        ans=sumt(c)-sumt(b-1)
        print(ans)