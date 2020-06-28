N,S = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
if len(arr)>1:
    for i in range(1,len(arr)):
        arr[i] = arr[i-1]+arr[i]
print(arr)