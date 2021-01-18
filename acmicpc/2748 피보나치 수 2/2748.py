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
dp = [-1]*91
dp[0]=0
dp[1]=1
dp[2]=1
def fibo(n):
    if dp[n]!=-1:
        return dp[n]
    dp[n]=fibo(n-1)+fibo(n-2)
    return dp[n]
num = ii()
print(fibo(num))