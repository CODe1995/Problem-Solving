N = int(input())
dp = [0]*1001
dp[1] = 10
dp[2] = 55

for i in range(3,N+1):
    temp = dp[i-1]-dp[i-2]
    dp[i]+=dp[i-1]+temp
    for j in range(9,-1,-1):
        temp-=j
        dp[i] += temp
print(dp[N]%10007)