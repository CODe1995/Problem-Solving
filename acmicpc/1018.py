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
        flag = 'W' if flag=='B' else 'B'        
    flag = 'W' if flag=='B' else 'B'
for i in range(n):
    print(boardW[i])
print()
for i in range(n):
    print(boardB[i])
# for i in range(n):
#     for j in range(m):
#         if j+8<=m and i+8<=n:
#             print(i,j,'==')
#             # print(boardW[j:j+8][i:i+8])
#             # print(boardB[j:j+8][i:i+8])

#             for w in boardW[i:i+8]:
#                 print(sum(w[j:j+8]),end=':')
#                 for inw in w[j:j+8]:
#                     print(inw,end=' ')

#                 print()
#             print('B')
            
#             for w in boardB[i:i+8]:
#                 print(sum(w[j:j+8]),end=':')
#                 for inw in w[j:j+8]:
#                     print(inw,end= ' ')
#                 print()
