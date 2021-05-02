N = int(input())
arr = list(map(int,input().split()))
start = arr[0]
end = arr[0]
answer = 0
for i in range(1,N):
    if end < arr[i]:
        end=arr[i]
    else:
        answer = max(end-start,answer)
        start = arr[i]
        end = arr[i]

print(max(answer,end-start))