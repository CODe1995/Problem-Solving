import sys
input = sys.stdin.readline

N,M = map(int,input().rstrip().split())
array = []
dp = [[0]*(M+1) for _ in range(N+1)]
for i in range(1,N+1):
    array.append(list(map(int,input().rstrip().split())))
for y in range(1,N+1):
    for x in range(1,M+1):
        dp[y][x] = array[y-1][x-1] + dp[y][x-1] + dp[y-1][x]-dp[y-1][x-1]

K = int(input())
for _ in range(K):
    i,j,x,y = map(int,input().rstrip().split())
    answer = dp[x][y] - dp[x][j-1] - dp[i-1][y] + dp[i-1][j-1]
    print(answer)