def solution(triangle):
    global answer
    dp = [[0]*len(triangle) for _ in range(len(triangle))]
    
    for i in range(len(triangle)):
        dp[len(triangle)-1][i] = triangle[len(triangle)-1][i]
    
    for i in range(len(triangle)-2,-1,-1):
        for j in range(len(triangle[i])):
            dp[i][j]=max(dp[i+1][j],dp[i+1][j+1])+triangle[i][j]
    
    # for i in dp:
    #     print(i)
    answer = dp[0][0]    
    return answer