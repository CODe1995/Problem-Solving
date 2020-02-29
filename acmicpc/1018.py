n,m = map(int,input().split())
board = [list(input()) for _ in range(n)]
cnt=[0,0]
for cost in range(2):
    if cost==0:turn='B'
    else: turn='W'
    for i in range(n):
        for j in board[i]:
            if cost==0:#BW
                if j != turn:       
                    cnt[cost]+=1
            elif cost==1:#WB
                if j != turn:       
                    cnt[cost]+=1
            
            if turn=='B':turn='W'
            else: turn='B'
print(cnt)