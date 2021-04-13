import sys
input = sys.stdin.readline
V,E = map(int,input().split())
INF = 10e9
dp = [[0]*(V+1) for _ in range(V+1)]

for i in range(E):
    s,e,d = map(int,input().split())
    dp[s][e]=d

for k in range(1,V+1):
    for i in range(1,V+1):
        for j in range(1,V+1):
            if dp[i][k] and dp[k][j]:
                dp[i][j] = min(dp[i][j],dp[i][k]+dp[k][j])
answer = 10e9

for i in range(1,V+1):    
    for j in range(1,V+1):
        if i==j:continue
        if dp[i][j] and dp[j][i]:
            answer = min(answer,dp[i][j]+dp[j][i])
    
print(-1 if answer==10e9 else answer)