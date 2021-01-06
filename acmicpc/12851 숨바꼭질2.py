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
arr = [[-1,0] for _ in range(maxnum)]

def solve():    
    q=deque([n])
    arr[n]=[0,1]#초기화    
    while q:
        x = q.popleft()
        for i in [x+1,x-1,x*2]:
            if 0<=i<maxnum:
                if arr[i][0]==-1:#첫방문
                    arr[i] = [arr[x][0]+1,arr[x][1]]
                    q.append(i)
                elif arr[i][0]==arr[x][0]+1:#처음 아닌경우
                    arr[i][1]+=arr[x][1]#중복되는 횟수를 더해줌    
solve()
print(arr[k][0])
print(arr[k][1])