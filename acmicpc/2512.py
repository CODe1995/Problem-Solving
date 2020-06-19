import sys
input = sys.stdin.readline
n = int(input().rstrip())
arr = list(map(int,input().rstrip().split()))
m = int(input().rstrip())
arr.sort()
start=1
end=arr[-1]
while start<=end:
    mid = (start+end)//2
    total =0
    for i in arr:
        if i > mid:
            total+=mid
        else:
            total+=i
    
    if total <= m:
        start = mid+1
    else:
        end = mid-1
print(end)
