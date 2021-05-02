N = int(input())
arr = list(map(int,input().split()))
sumArr = [arr[i] for i in range(N)]
for i in range(N):
    for j in range(i):
        if arr[i]>arr[j]:
            sumArr[i] = max(sumArr[i],sumArr[j]+arr[i])
print(max(sumArr))