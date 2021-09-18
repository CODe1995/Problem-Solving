D,P = map(int,input().split())
answer = -1
visited = {}
def getLength(num):
    cnt = 0
    while num>0:
        num//=10
        cnt+=1
    return cnt
def calc(depth,res):
    global D,P,answer,visited
    if getLength(res) > D or (depth,res) in visited:
        return
    if depth == P:
        answer = max(answer,res)
        return
    visited[(depth,res)] = True#깊이에 따른 최대값 변경
    for i in range(2,10):
        calc(depth+1,res*i)
    return    
calc(0,1)
print(answer)