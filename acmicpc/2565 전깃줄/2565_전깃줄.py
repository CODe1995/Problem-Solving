import sys
input = sys.stdin.readline

N = int(input())
lines = [list(map(int,input().strip().split())) for _ in range(N)]
lines = sorted(lines,key = lambda x:x[0])
dp = [1]*N
for i in range(N):
    for j in range(i):
        if lines[i][1]>lines[j][1]:
            if dp[j]+1>dp[i]:
                dp[i]=dp[j]+1
print(N-max(dp))