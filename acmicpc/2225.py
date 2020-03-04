N,K = map(int,input().split())
dp = [[0]*(K+1) for _ in range(N+1)]  #200*200 크기 생성
for i in range(1,N+1):dp[i][1]=1    #K가 1일땐 모두 1
for i in range(2,K+1):dp[1][i]=dp[1][i-1]+1 #1일때 칸 채우기
for i in range(2,N+1):
    for j in range(2,K+1):
        dp[i][j] = dp[i][j-1]+dp[i-1][j]
print(dp[-1][-1]%1000000000)
