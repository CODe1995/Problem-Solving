N = int(input())
month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
answer = 0
day = 1
# visited = [[-1]*367 for _ in range(7)]
for year in range(2019,N+1):
    # thisYear = 0
    # beforeDay = day
    if (year%100!=0 and year%4==0) or (year%400==0):month[2]=29
    else: month[2]=28

    # if visited[beforeDay][sum(month)]>=0:
    #     answer += visited[beforeDay][sum(month)]
    #     day = (day+sum(month)%7)%7
        

    for mth in range(1,13):
        if (day+13)%7-1==4:
            answer+=1
            # thisYear+=1
        day = (day+month[mth])%7
    # afterDay = day
    # if visited[beforeDay][sum(month)]==-1:
    #     visited[beforeDay][sum(month)]=thisYear
print(answer)
