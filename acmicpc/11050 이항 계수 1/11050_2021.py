n,r = map(int,input().split())
dp = [[0]*11 for _ in range(11)]
for i in range(11):
    for j in range(i+1):
        if i==j or i<=0 or j<=0:dp[i][j]=1
        else: dp[i][j]=dp[i-1][j]+dp[i-1][j-1]
print(dp[n][r])