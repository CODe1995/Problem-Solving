import sys
input = sys.stdin.readline
INF = 10e9
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
dp = [[INF]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i==j:dp[i][j]=0
        elif arr[i][j]:dp[i][j]=arr[i][j]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if dp[i][k]==1 and dp[k][j]==1:
                dp[i][j] = 1                

for line in dp:
    for x in line:
        print(0 if x==INF else x,end=' ')
    print()