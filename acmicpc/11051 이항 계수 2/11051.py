n,r = map(int,input().split())
dp = [[0]*1001 for _ in range(1001)]
for i in range(1,1001):
    for j in range(i+1):
        if i==j or j==0:dp[i][j]=1
        else: dp[i][j] = (dp[i-1][j]+dp[i-1][j-1])%10007
print(dp[n][r])