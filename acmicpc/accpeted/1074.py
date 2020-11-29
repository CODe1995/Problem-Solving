n,r,c = map(int,input().split())
cnt = 0
direction = [[0,0],[1,0],[0,1],[1,1]]
def solve(size, x, y):
    global cnt
    # print(size,'(',x,',',y,')',cnt)
    if size==2:
        for dx,dy in direction:
            nx = dx+x
            ny = dy+y
            if nx==c and ny==r:
                print(int(cnt))
                return
            cnt+=1
    else:
        solve(size/2,x,y)#leftTop
        solve(size/2,x+size/2,y)#rightTop
        solve(size/2,x,y+size/2)#leftDown
        solve(size/2,x+size/2,y+size/2)#rightDown
def whrQuadrant(size,x,y):#좌표 입력하면 몇사분면인지 반환
    if size/2<=x and size/2>y:#1사분면
        return (size/2)**2, size/2,0
    if size/2>x and size/2>y:#2사분면
        return 0,0,0
    if size/2>x and size/2<=y:#3사분면
        return ((size/2)**2) * 2,0,size/2
    if size/2<=x and size/2<=y:#4사분면
        return ((size/2)**2) * 3,size/2,size/2
size = 2**n
cnt,x,y = whrQuadrant(size,c,r)
solve(size,x,y)