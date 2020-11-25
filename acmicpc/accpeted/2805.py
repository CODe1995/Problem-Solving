n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
start,end = 1,arr[-1]
while start<=end:
    mid = (start+end)//2
    total = 0
    for i in arr:
        if i > mid:
            total += i-mid
    if total >= m:
        start = mid+1
    else:
        end = mid-1
print(end)