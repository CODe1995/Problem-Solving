from collections import deque,defaultdict
n,m,v = map(int,input().split())
arr=[]
verset=defaultdict(list)
for i in range(m):
    arr.append(list(map(int,input().split())))
    verset[arr[i][0]].append(arr[i][1])
    verset[arr[i][1]].append(arr[i][0])
for i in range(1,m+1):
    verset[i]=set(verset[i])
# print(verset)

def dfs(graph,root):
    visited = []
    stack = [root]

    return

root=v
print(dfs(verset,root))
# print(bfs(verset,root))