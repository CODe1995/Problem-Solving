##########################################################
import sys
input = sys.stdin.readline
def ii():return int(input())
def mii():return map(int,input().rstrip().split())
def lmii():return list(map(int,input().rstrip().split()))
##########################################################

#창고의 가로,세로 / 상자의 개수
clx, cly, n = mii()
for _ in range(n):
    #상자의 가로,세로,높이 / 쌓아야하는 위치
    lx,ly,lz,px,py = mii()

