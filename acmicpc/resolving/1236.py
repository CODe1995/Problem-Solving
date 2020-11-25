height,width = map(int,input().split())
castle = []
Xchecker_height = [0]*width
Xchecker_width = [0]*height
for _ in range(height):
    s=list(input())
    castle.append(s)
cRow=0    #열
cCol=0    #행
cnt = 0
for i in range(height):
    if 'X' in castle[i]:
        Xchecker[i]=1
for i in range(height):
    if 'X' not in castle[i]:
        idx = 0
        if 0 in Xchecker:
            idx = Xchecker.index(0)
            Xchecker[idx]=1
        castle[i][idx]='X'        
        cnt+=1

    for k in castle:
        print(k)
    print()
print(cnt)