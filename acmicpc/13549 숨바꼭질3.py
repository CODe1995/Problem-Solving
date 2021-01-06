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
arr = [0]*maxnum

def solve():    
    q=deque([n])
    
    while q:
        x = q.popleft()

        for i in [x+1,x-1,x*2]:
            if 0<=i<maxnum and arr[i]==0:
                if i==x*2:
                    arr[i]=arr[x]
                else:
                    arr[i]=arr[x]+1
                if i==k:
                    return arr[i]
                q.append(i)
print(solve())