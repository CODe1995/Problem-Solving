import sys
def bs(arr,tr,low,high):
    if low>high:return False
    mid=(low+high)//2
    if tr<arr[mid]:
        return bs(arr,tr,low,mid-1)
    elif tr > arr[mid]:
        return bs(arr,tr,mid+1,high)
    else:#같다
        return True
inp = sys.stdin.readline
n=int(input())
arr1 = sorted(list(map(int,inp().rstrip().split())))
m=int(input())
arr2 = list(map(int,inp().rstrip().split()))

for tr in arr2:
    if bs(arr1,tr,0,n-1):
        print(1)
    else:
        print(0)
