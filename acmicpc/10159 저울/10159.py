import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
dp = [[0]*(N+1) for _ in range(N+1)]

for i in range(M):
    a,b = map(int,input().split())
    dp[a][b]=1

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if dp[i][k] and dp[k][j]:
                dp[i][j]=1

for i in range(1,N+1):
    cnt = 0
    for j in range(1,N+1):
        if dp[i][j] or dp[j][i]:
            cnt+=1
    print(N-cnt-1)