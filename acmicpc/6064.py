import sys
from math import gcd
input = sys.stdin.readline
def ii():return int(input())
def mii():return map(int,input().rstrip().split())
def lmii():return list(map(int,input().rstrip().split()))

def lcm(a,b):
    r=gcd(a,b)
    return r*a//r*b//r

t = ii()
for _ in range(t):
    m,n,x,y, = mii()
    mx = lcm(m,n)
    print('mx %d'%mx)
    s,e = 0,0
    cnt=0
    while m*s+n*e<=mx-(x+y)  and s<=m and e<=n:        
        e=0
        while m*s+n*e<=mx-(x+y) and s<=m and e<=n:
            cnt+=1
            e+=1
        s+=1
        
    print(s,e,cnt)