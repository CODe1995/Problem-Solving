import sys
input = sys.stdin.readline

N,M = map(int,input().rstrip().split())
array = []
for _ in range(N):
    tmp = list(map(int,input().rstrip().split()))
    array.append(tmp)
for x in range(M):
    for y in range(N):
        if x==0 and y==0:
            pass
        elif y==0 and x>=1:
            array[y][x]+=array[N-1][x-1]
        else:
            array[y][x]+=array[y-1][x]
K=int(input())

#i j x y
for _ in range(K):
    sY,sX,eY,eX = map(int,input().rstrip().split())
    sY-=1
    sX-=1
    eY-=1
    eX-=1

    if sX==0 and sY==0:
        print(array[eY][eX])
    elif sX>=1 and sY==0:
        print(array[eY][eX]-array[N-1][sX-1])
    else:
        print(array[eY][eX]-array[sY-1][sX])
    # if i-1==0:
    #     if j-1>=1:
    #         j-=1
    #         i=M-1
    #         print(array[x][y]-array[i][j])
    #     else:
    #         print(array[x][y])
    # else:        
    #     print(array[x][y]-array[i-1][j])