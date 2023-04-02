# https://jaemin8852.tistory.com/163

import sys
input = sys.stdin.readline

N, K = map(int,input().split())
arr = [0] + [int(input()) for _ in range(N)]
dp = [100001] * (10001)
dp[0] = 0

for i in range(1,N+1):
    for j in range(arr[i], K+1):
        dp[j] = min(dp[j-arr[i]] + 1, dp[j])

print(dp[K] if dp[K] != 100001 else -1)