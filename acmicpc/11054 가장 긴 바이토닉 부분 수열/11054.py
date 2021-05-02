N = int(input())
arr = list(map(int,input().split()))
length_INC = [1]*N
length_DEC = [1]*N
for i in range(N):#LIS_증가
    for j in range(i):
        if arr[i]>arr[j] and length_INC[i]<length_INC[j]+1:
            length_INC[i]=length_INC[j]+1
for i in range(N-1,-1,-1):#LIS_감소
    for j in range(N-1,i,-1):
        if arr[i]>arr[j] and length_DEC[i]<length_DEC[j]+1:
            length_DEC[i] = length_DEC[j]+1
answer = 0
for i in range(N):
    answer = max(length_DEC[i]+length_INC[i]-1,answer)
print(answer)