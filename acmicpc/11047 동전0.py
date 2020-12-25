##########################################################
import sys
input = sys.stdin.readline
def ii():return int(input())
def mii():return map(int,input().rstrip().split())
def lmii():return list(map(int,input().rstrip().split()))
##########################################################
n,k = mii()
lst = list()
for _ in range(n):
    lst.append(ii())
lst.sort(reverse=True)
cnt = 0
for i in lst:
    cnt+=k//i
    k%=i
print(cnt)