N,M,H = map(int,input().split())
ladders = [[0]*N for _ in range(H)]
answer = -1
for i in range(M):
    a,b = map(int,input().split())
    ladders[a-1][b-1]=1
    ladders[a-1][b]=-1

def checkLadders():
    for ladder in range(N):
        x = ladder
        y = 0
        moved = False
        while y<H:
            if ladders[y][x]==0 or moved:
                y+=1
                moved = False
            elif ladders[y][x]==1 and not moved:
                x+=1
                moved = True
            elif ladders[y][x]==-1 and not moved:
                x-=1
                moved = True
        if x!=ladder:
            return False
    return True

def dfs(depth, number):
    global answer
    if checkLadders():
        if answer==-1:answer = depth
        else: answer = min(answer,depth)
        return
    if depth == 3:
        return    
    for next_number in range(number,N*H):
        x,y = next_number%N, next_number//N
        if ladders[y][x]==0:
            if x+1<N and ladders[y][x+1]==0:
                ladders[y][x]=1
                ladders[y][x+1]=-1
                dfs(depth+1,next_number+1)
                ladders[y][x]=0
                ladders[y][x+1]=0                

dfs(0,0)
print(answer)