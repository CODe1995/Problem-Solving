import sys
input = sys.stdin.readline
N = int(input())
field = [list(map(int,input().strip().split())) for _ in range(N)]
direction = [[1,0],[1,1],[0,1]]#우,우하,하
dp =  [[[0]*N for _ in range(N)] for _ in range(3)]
dp[0][0][1]=1#시작점
for j in range(2,N):#가로 첫 열 먼저 체크
    if field[0][j]==0:
        dp[0][0][j] = dp[0][0][j-1]
for i in range(1,N):
    for j in range(1,N):
        if field[i][j]==0 and field[i-1][j]==0 and field[i][j-1]==0:#대각체크
            dp[1][i][j] = dp[0][i-1][j-1]+dp[1][i-1][j-1]+dp[2][i-1][j-1]
        if field[i][j]==0:#세로,가로체크
            dp[0][i][j]=dp[0][i][j-1]+dp[1][i][j-1]
            dp[2][i][j]=dp[2][i-1][j]+dp[1][i-1][j]
n=N-1
ans = dp[0][n][n]+dp[1][n][n]+dp[2][n][n]
print(ans)