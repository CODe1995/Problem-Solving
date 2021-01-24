#https://st-lab.tistory.com/115
n,m = map(int,input().split())
arr = [0]*n
def dfs(at,depth):
    if depth==m:
        for a in arr:
            if a != 0:
                print(a,end=' ')                
        print()
        return
    for i in range(at,n+1):     
            arr[depth] = i
            dfs(i+1,depth+1)
dfs(1,0)