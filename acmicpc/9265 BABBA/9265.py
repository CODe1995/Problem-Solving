k = int(input())
dp = [0]*46
dp[0] = [1,0]
dp[1] = [0,1]
dp[2] = [1,1]
for i in range(3,k+1):
    dp[i] = [dp[i-1][0]+dp[i-2][0],dp[i-1][1]+dp[i-2][1]]
print(dp[k][0],dp[k][1])