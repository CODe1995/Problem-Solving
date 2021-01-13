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
n,k = mii()
arr = lmii()

#표준편차를 반환하는 함수
def sdFunc(target):
    dis = 0
    avg = sum(target)/len(target)#산술평균
    for z in target:
        dis+=(z-avg)**2
    return dis/len(target)#분산 반환

answer = list()
for i in range(n-k+1):#K개 이상의 = n-k
    for j in range(n-k-i+1):#해당 범위로 리스트를 훑음
        tmp = arr[i:i+k+j]
        a = sdFunc(tmp)
        answer.append(a)
print(math.sqrt(min(answer)))