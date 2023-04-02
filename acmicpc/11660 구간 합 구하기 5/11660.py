import sys
N, M = map(int, input().split())
fields = [[0] * (N+1)]

for i in range(1, N+1):
    line = [0] + list(map(int,input().split()))
    fields.append(line)

for i in range(1,N+1):
    for j in range(1, N+1):
        fields[i][j] = fields[i][j-1] + fields[i][j] + fields[i-1][j] - fields[i-1][j-1]


for _ in range(M):
    y1, x1, y2, x2 = map(int, sys.stdin.readline().rstrip().split())
    answer = fields[y2][x2] - fields[y2][x1-1] - fields[y1-1][x2] + fields[y1-1][x1-1]
    print(answer)
 