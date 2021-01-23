import sys
N,M = map(int,input().split())
arr = [0]*N
visit = [False]*N

def dfs(depth):
    if depth == M:
        for a in arr:
            if not a==0:
                # print(a,end=' ')
                sys.stdout.write(str(a)+" ")
        # print()
        sys.stdout.write("\n")
        return
    for i in range(N):
        if not visit[i]:
            visit[i]=True
            arr[depth]=i+1
            dfs(depth+1)
            visit[i]=False    
dfs(0)