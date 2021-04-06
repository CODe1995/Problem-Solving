import sys
input = sys.stdin.readline
N,M = map(int,input().split())
field=[list(map(int,list(input().strip()))) for _ in range(N)]
dp = [[0]*M for _ in range(N)]
answer = 0
for i in range(N):
    for j in range(M):
        if field[i][j]==1:
            # if dp[i][j]==0:dp[i][j]=1
            # if 0<=j-1<M and 0<=i-1<N:
            #     dp[i][j]=max(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])
            #     if dp[i][j]==dp[i-1][j]==dp[i-1][j-1]==dp[i][j-1]:
            #         dp[i][j]+=1
            #     if dp[i-1][j]==0 or dp[i-1][j-1]==0 or dp[i][j-1]==0:
            #         dp[i][j]=1
            dp[i][j] = min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])+1
        answer = max(answer,dp[i][j])
print(answer**2)        