n,m = map(int,input().split())
board = [list(input()) for _ in range(n)]
boardW = [[0]*m for _ in range(n)]
boardB = [[0]*m for _ in range(n)]

flag = 'W'
for i in range(n):
    for j in range(m):
        if board[i][j]==flag:
            boardW[i][j]=0
            boardB[i][j]=1
        else:
            boardW[i][j]=1
            boardB[i][j]=0
        if j+1!=m:
            flag = 'W' if flag=='B' else 'B'  
    if m%2!=0:
        flag = 'W' if flag=='B' else 'B'  

res=99999999
for i in range(n):
    for j in range(m):
        if j+8<=m and i+8<=n:
            sumW=0
            sumB=0
            for w in boardW[i:i+8]:
                sumW+=sum(w[j:j+8])
            
            for b in boardB[i:i+8]:
                sumB+=sum(b[j:j+8])
        res=min(sumW,sumB,res)
print(res)