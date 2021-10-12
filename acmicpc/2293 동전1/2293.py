import sys

input = sys.stdin.readline
N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
dp = [0]*10001
dp[0] = 1
for i in range(N):
    for j in range(coins[i],K+1):
        dp[j]+=dp[j-coins[i]]
print(dp[K])