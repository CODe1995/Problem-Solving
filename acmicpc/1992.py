k = int(input())
arr = [[0]*k for _ in range(k)]
def quadTree(size, x, y):
    prev = arr[y][x]
    flag = True
    for i in range(size):
        if flag==False:
            break
        for j in range(size):
            nx = int(x+j)
            ny = int(y+i)
            if arr[ny][nx] != prev:
                flag=False
                break
    if  flag==True:
        print(prev,end='')
    else:
        print('(',end='')
        quadTree(int(size/2),x,y)#leftTop
        quadTree(int(size/2),x+size//2,y)#rightTop
        quadTree(int(size/2),x,y+size//2)#leftDown
        quadTree(int(size/2),x+size//2,y+size//2)#rightDown        
        print(')',end='')
            
for i in range(k):
    arr[i] = list(map(int,input()))
quadTree(k,0,0)