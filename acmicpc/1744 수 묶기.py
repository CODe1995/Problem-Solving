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
arr.sort()
ans=0
left,right = 0 , n-1
for _ in range(right,left,-2):#양수
    a,b = arr[right],arr[right-1]
    if a>1 and b>1:ans+=a*b
    else:break
    right-=2
# print('plus',ans)
for _ in range(left,right,2):#음수
    a,b = arr[left],arr[left+1]
    if a<=0 and b<=0:ans+=a*b
    else:break
    left+=2
# print('minus',ans)
for k in range(left,right+1):
    ans+=arr[k]
print(ans)