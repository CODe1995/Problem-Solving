##########################################################
import sys
input = sys.stdin.readline
def ii():return int(input())
def mii():return map(int,input().rstrip().split())
def lmii():return list(map(int,input().rstrip().split()))
##########################################################
n = ii()
arr = lmii()
arr.sort()
# print(arr)
ans = 0
for i in range(1,n):
    arr[i] += arr[i-1]
print(sum(arr))