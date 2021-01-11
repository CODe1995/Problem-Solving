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
n = ii()#보드의 크기
k = ii()#사과의 개수
apple = deque()
for _ in k:
    apple.append(lmii())
l = ii()#뱀의 방향 변환 횟수
turn = deque()
for _ in l:
    a,b = lip()
    turn.append([int(a),b])
apple.sort()
turn.sort()

# 사과를 다 먹은경우
# 