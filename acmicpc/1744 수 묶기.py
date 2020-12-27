##########################################################
import sys
input = sys.stdin.readline
def ip():return input().rstrip()
def lip():return list(input().rstrip())
def ii():return int(input())
def mii():return map(int,input().rstrip().split())
def lmii():return list(map(int,input().rstrip().split()))
##########################################################
n = ii()
arr = list()
for _ in range(n):
    arr.append(ii())
arr.sort(reverse=True)
# print(arr)
# 음수와 음수
# 가장 큰 수 2개
i,j=0,n-1
ans=0
if n==1:
    print(sum(arr))
    sys.exit()
while i<n:#양수만
    res = arr[i]*arr[i+1]
    if arr[i]<0 and arr[i+1]<0:break
    if res>0:
        ans+=res
        i+=2
    else:#음수 또는 0인 경우
        break
while j-1>i:#음수 또는 0
    res = arr[j]*arr[j-1]
    ans+=res
    j-=2
print(ans)