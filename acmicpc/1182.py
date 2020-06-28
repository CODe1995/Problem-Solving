N,S = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()

def dynamic_programming(arrs):
    cache = [None] * len(arrs)
    cache[0] = arr[0]

    for i in range(1,len(arr)):
        cache[i] = max(0,cache[i-1])+arr[i]
    
    return max(cache)


if len(arr)>1:
    for i in range(1,len(arr)):
        arr[i] = arr[i-1]+arr[i]
print(arr)
print(dynamic_programming(arr))