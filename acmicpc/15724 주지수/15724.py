import sys
input = sys.stdin.readline
print = sys.stdout.write
N,M = map(int,input().split())

field = [list(map(int,input().strip().split())) for _ in range(N)]
sum_field = [[0]*(M+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,M+1):
        sum_field[i][j] = field[i-1][j-1] + sum_field[i][j-1] + sum_field[i-1][j] - sum_field[i-1][j-1]

K = int(input())

for i in range(K):
    y1,x1,y2,x2 = map(int,input().split())
    print(str(sum_field[y1-1][x1-1]+sum_field[y2][x2]-sum_field[y1-1][x2]-sum_field[y2][x1-1])+'\n')
