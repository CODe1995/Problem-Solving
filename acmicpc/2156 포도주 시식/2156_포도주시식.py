import sys
input = sys.stdin.readline
N = int(input())
arr = list(int(input()) for _ in range(N))
dp = [0]*N

# N, N-1, N-3
# N, N-2, N-3

dp[0] = arr[0]  #첫번째 잔 선택
dp[1] = arr[0]+arr[1]   #첫번째 두번째 선택
#첫번째 세번째, 두번째 세번째, 첫번째 두번째 중  최댓값 선택
dp[2] = max(arr[2]+arr[0],arr[2]+arr[1],dp[1])
for i in range(3,N):
    dp[i] = arr[i] + max(dp[i-3]+arr[i-1],dp[i-2])
    dp[i] = max(dp[i],dp[i-1])

print(dp[N-1])