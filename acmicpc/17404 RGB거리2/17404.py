import sys
input = sys.stdin.readline
N = int(input())
arr = [list(map(int,input().strip().split())) for _ in range(N)]
dp = [[1001*1001+1]*3 for _ in range(N)]
answer = 10e9
for color in range(3):    
    for i in range(3):
        if i==color:
            dp[0][color]=arr[0][color]
        else:
            dp[0][i]=1001*1001+1
    for i in range(1,N):
        dp[i][0] = min(dp[i-1][1],dp[i-1][2])+arr[i][0]
        dp[i][1] = min(dp[i-1][0],dp[i-1][2])+arr[i][1]
        dp[i][2] = min(dp[i-1][0],dp[i-1][1])+arr[i][2]
    for i in range(3):
        if i!=color:
            answer = min(answer,dp[N-1][i])
print(answer)