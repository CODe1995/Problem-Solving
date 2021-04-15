import sys
input = sys.stdin.readline
N,M = map(int,input().split())
INF = 10e9
arr = [[INF]*(N+1) for _ in range(N+1)]
dp = [[0]*(N+1) for _ in range(N+1)]
graph = dict()
for i in range(1,N+1):
    graph[i]=list()
for i in range(M):
    a,b,c = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    arr[a][b]=c
    arr[b][a]=c
    dp[a][b]=b
    dp[b][a]=a
for i in range(1,N+1):
    arr[i][i]=0
for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1): 
            if arr[i][j]>arr[i][k]+arr[k][j]:
                arr[i][j]=arr[i][k]+arr[k][j]
                dp[i][j]=dp[i][k]

for i in range(1,N+1):
    for j in range(1,N+1):
        print('-' if dp[i][j]==0 else dp[i][j],end=' ')
    print()
