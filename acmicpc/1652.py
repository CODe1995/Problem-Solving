def calc(line):
    ln = len(line)
    offset = -1
    cnt=0
    for i in range(1,ln):
        if line[i-1]=='.' and line[i] == '.' and offset==-1:
            offset=i-1
        if (line[i]=='X' or i==ln-1) and i-offset>=1 and offset!=-1:
            cnt+=1
            offset=-1
        elif line[i]=='X':
            offset=-1
    return cnt

N = int(input())
room = [list(map(str,input()))for _ in range(N)]
rsum=0;csum=0
for i in range(N):
    rsum+=calc(room[i])
for i in range(N):
    csum+=calc(list(room[j][i] for j in range(N)))
print(rsum,csum)
        


