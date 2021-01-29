import sys
input = sys.stdin.readline
N,M = map(int,input().rstrip().split())
comp = [['W' if (i+j)%2==0 else 'B' for i in range(N)] for j in range(M)]
field = [list(input().rstrip()) for _ in range(N)]
answer = 2501
for b_i in range(N-7):
    for b_j in range(M-7):
        cnt = [0,0]
        for h in range(b_i,b_i+8):
            for w in range(b_j,b_j+8):
                if comp[h-b_i][w-b_j]!=field[h][w]:cnt[0]+=1
                else:cnt[1]+=1
        minNum = min(cnt[0],cnt[1])
        if answer > minNum:answer=minNum
print(answer)