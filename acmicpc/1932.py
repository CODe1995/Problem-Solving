import math
n = int(input())
trg = []
dp =[]
for i in range(n):
    trg.append(list(map(int,input().split())))

# 자기자신과 같은 넘버와 그 다음 넘버를 더할 수 있다.
# 처음과 끝이 아닌 애들은 무조건 2개의 수를 갖는다. 그래서 max처리 해주자.

for i in range(n-1):
    for j in range(len(trg[i+1])):
        # out of range 에러
        # if (j==0 or j==len(trg[i+1])-1):#처음이거나 끝이면
        #     trg[i+1][j] = trg[i][j]+trg[i+1][j]
        if (j==0):
            trg[i+1][j] = trg[i][j]+trg[i+1][j]
        elif (j==len(trg[i+1])-1):
            trg[i+1][j] = trg[i][-1] + trg[i+1][-1]
        else:#중간이면
            trg[i+1][j] = max(trg[i][j-1]+trg[i+1][j],trg[i][j]+trg[i+1][j])
print(max(trg[n-1]))


