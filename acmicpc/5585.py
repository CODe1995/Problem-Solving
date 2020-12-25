##########################################################
import sys
input = sys.stdin.readline
def ii():return int(input())
def mii():return map(int,input().rstrip().split())
def lmii():return list(map(int,input().rstrip().split()))
##########################################################
n = 1000-ii()
lst = [500,100,50,10,5,1]
cnt = 0
for i in lst:
    cnt+=n//i
    n%=i
print(cnt)