cnt = 0
N,S = None,None

def dfs(i, su):
    global cnt
    if i==N: return
    if su+arr[i] == S:
        cnt+=1
    dfs(i+1,su)    
    dfs(i+1,su+arr[i])

N,S = map(int,input().split())
arr = list(map(int,input().split()))
dfs(0,0)
print(cnt)