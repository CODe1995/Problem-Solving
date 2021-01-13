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
import math
n=ii()
a = lmii()
b,c = mii()

answer = 0
for i in a:
    if i-b<=0:#총감독관으로도 커버 되는 경우
        answer+=1
    else:
        t = (i-b)/c 
        answer+=1+math.ceil(t)
print(answer)