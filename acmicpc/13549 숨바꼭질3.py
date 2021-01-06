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
arr = [-1]*maxnum

def solve():    
    q=deque([n])
    arr[n]=0
    while q:
        x = q.popleft()        
        if x==k:
            return arr[x]
        for i,j in [[x-1,0],[x*2,2],[x+1,1]]:
            if 0<=i<maxnum and arr[i]==-1:
                if j==2:
                    arr[i]=arr[x]
                else:
                    arr[i]=arr[x]+1
                q.append(i)
print(solve())