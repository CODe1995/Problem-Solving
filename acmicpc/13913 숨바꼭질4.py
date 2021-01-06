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
maxnum = 100001
n,k = mii()
arr = [[-1,[n]] for _ in range(maxnum)]

def solve():    
    q=deque([n])
    arr[n][0]=0#초기화    
    while q:
        x = q.popleft()
        if x==k:
            return
        for i in [x+1,x-1,x*2]:
            if 0<=i<maxnum:
                if arr[i][0]==-1:#첫방문
                    arr[i][0] = arr[x][0]+1
                    arr[i][1]=arr[x][1]+[i]
                    q.append(i)
solve()
print(arr[k][0])
for a in arr[k][1]:
    print(a,end=' ')