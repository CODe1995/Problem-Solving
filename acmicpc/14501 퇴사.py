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
n=ii()
arr = deque()
for _ in range(n):
    arr.append(lmii())
answer =0
i=0
while i<n:
    a,b=arr[i]
    i+=a
    if i-1<n:
        answer+=b
print(answer)