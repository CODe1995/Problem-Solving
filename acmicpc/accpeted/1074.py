n,r,c = map(int,input().split())
array = [[0]* 2**n for _ in range(2**n)]
cnt = 0
def solve(size, x, y):
    global cnt
    # print(size,'(',x,',',y,')',cnt)
    if size==1:
        if x==c and y==r:
            print(cnt)
            return
        cnt+=1
    else:
        solve(size/2,x,y)#leftTop
        solve(size/2,x+size/2,y)#rightTop
        solve(size/2,x,y+size/2)#leftDown
        solve(size/2,x+size/2,y+size/2)#rightDown
solve(2**n,0,0)