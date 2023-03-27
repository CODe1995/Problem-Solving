N, M = map(int, input().split())
An = [0] + list(map(int, input().split()))
Mn = [0] + list(map(int, input().split()))

sumCost = sum(Mn)

dp = [[0]*(sumCost+1) for _ in range(N+1)]
answer = 100001

for i in range(1, N+1):
    app = An[i]
    cost = Mn[i]

    for j in range(1, sumCost+1):
        if j - cost >= 0: # 현재 앱의 cost가 끌 수 있는 cost인지 확인
            # 현재 앱을 끈 뒤의 byte와 그냥 켜둔 byte를 비교 
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost] + app)
        else:
            dp[i][j] = dp[i-1][j]
        if dp[i][j] >= M:
            answer = min(answer, j)
print(answer)