import sys
input = sys.stdin.readline
def ii():return int(input())
def mii():return map(int,input().rstrip().split())
def lmii():return list(map(int,input().rstrip().split()))

x,y = mii()
z = y*100//x
left,right = 0,10**9
ans = -1
while left<=right:
    mid = (left+right)//2
    res = ((y+mid)*100)//(x+mid)
    if z<res:
        right = mid-1
        ans = mid
        # print(left,mid,right)
    else:
        left = mid+1
        # print(left,mid,right)
print(ans)