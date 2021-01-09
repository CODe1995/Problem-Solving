##########################################################
import sys
from collections import deque
direction = [[0,1],[-1,0],[1,0],[0,-1]] #for BFS
input = sys.stdin.readline
def ip():return input().rstrip()
def lip():return list(ip())
def ips():return ip().split()
def ii():return int(input())
def mii():return map(int,ips())
def lmii():return list(mii())
##########################################################
sys.setrecursionlimit(10**5)
maxnum = 100001
n,k = mii()

if n>k:
    print(n-k)
    for i in range(n,k-1,-1):
        print(i,end=' ')
    sys.exit()
elif n==k:
    print(0)
    print(n)
    sys.exit()
arr = [-1]*maxnum
tree = dict()
def solve():    
    q=deque([n])
    arr[n]=0#초기화
    # tree[n] = n
    while q:
        x = q.popleft()        
        if x==k:
            return
        for i in [x+1,x-1,x*2]:
            if 0<=i<maxnum:
                if arr[i]==-1 :#첫방문
                    tree[i]=x
                    arr[i] = arr[x]+1
                    q.append(i)
solve()
print(arr[k])
answer= deque()
def search(num):
    global answer
    answer.append(num)
    if num==n:return  
    tt = tree[num]     
    search(tt)
    

search(k)
for z in range(len(answer)-1,-1,-1):
    print(answer[z],end=' ')