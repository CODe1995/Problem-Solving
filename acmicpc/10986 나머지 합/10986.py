N,M = map(int,input().split())
arr = [0]+list(map(int,input().split()))
counter = [0]*M
for i in range(1,N+1):
    arr[i] = arr[i] + arr[i-1]
    arr[i] = arr[i] % M
    counter[arr[i]] = counter[arr[i]]+1
answer = counter[0]
for i in range(M):    
    answer = answer + (counter[i]*(counter[i]-1))//2
print(answer)