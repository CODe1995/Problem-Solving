N = int(input())
arr = list(map(int,input().split()))
length = [1]*N
maxLength = 1
for i in range(N):
    for j in range(i):
        if arr[j]>arr[i] and length[i]<length[j]+1:
            length[i] = length[j]+1
            maxLength = max(maxLength,length[i])
print(maxLength)