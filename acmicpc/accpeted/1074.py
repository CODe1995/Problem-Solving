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
                print(cnt)
                return
            cnt+=1
    else:
        solve(size/2,x,y)#leftTop
        solve(size/2,x+size/2,y)#rightTop
        solve(size/2,x,y+size/2)#leftDown
        solve(size/2,x+size/2,y+size/2)#rightDown
solve(2**n,0,0)