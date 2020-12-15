N=int(input())
snail = [[0]*N for i in range(N)]
for i in range(N*N):
    snail[N//2][N//2] = i
print(snail)