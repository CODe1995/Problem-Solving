N,M = map(int,input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))
for _ in range(M):
    a,b = map(int,input().split())
    a= a-1
    tmp = sorted(arr[a:b])
    print(tmp[0],tmp[b-a-1])