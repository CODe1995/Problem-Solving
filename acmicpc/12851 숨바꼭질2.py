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
fastest = maxnum#가장 빠른 시간 저장
cnt=0

def solve():    
    global fastest,cnt
    q=deque([n])
    while q:
        x = q.popleft()
        if x == k and fastest>=maxnum:
            fastest=arr[x]
            cnt+=1
        for i in [x+1,x-1,x*2]:
            if 0<=i<maxnum:
                if arr[i]==0 or arr[i]>=arr[x]+1:
                    if fastest<maxnum and fastest==arr[x]+1 and k==i:
                        cnt+=1
                    else:
                        arr[i] = arr[x]+1
                        q.append(i)
    return '{}\n{}'.format(arr[k],cnt)

print(solve())
