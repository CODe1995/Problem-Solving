import sys
input = sys.stdin.readline
N = int(input().rstrip())
dp = [0]*(N+1)
dp[1] = 9
for i in range(2,N+1):
    dp[i]=dp[i-1]*2-(i-1)
print(dp[-1])