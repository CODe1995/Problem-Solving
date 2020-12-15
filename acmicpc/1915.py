import sys
input = sys.stdin.readline
height,width = map(int,input().split())
arr = []
dp = [[0]*1001 for _ in range(1001)]
length = 0
for i in range(height):
    arr.append(list(map(int,list(input().strip()))))

for i in range(height):
    for j in range(width):
        if arr[i][j] == 1:
            dp[i][j]=min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])+1
            length = max(length,dp[i][j])
print(length**2)