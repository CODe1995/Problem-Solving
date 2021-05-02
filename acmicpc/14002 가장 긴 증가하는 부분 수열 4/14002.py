N = int(input())
arr = list(map(int,input().strip().split()))
LIS = [1] * N
rev = [-1] * N
maxLIS = 1  #LIS 최대 길이 저장
for i in range(N):
    for j in range(i):
        if arr[i]>arr[j] and LIS[i] < LIS[j]+1:
            LIS[i] = LIS[j]+1
            rev[i] = j
            maxLIS = max(maxLIS,LIS[i])
    
answer = list()
def find(x):    
    answer.append(arr[x])
    if(rev[x]==-1):        
        return -1
    return find(rev[x])

for i in range(N):
    if maxLIS == LIS[i]:
        find(i)
        break

print(len(answer))
for i in range(len(answer)-1,-1,-1):
    print(answer[i],end=' ')
