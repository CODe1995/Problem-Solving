import sys
input = sys.stdin.readline
tree = list()
nodes = list()

def update(start,end,index,left,right,changeNum):
    if left>end or right<start:return
    if start==end:
        tree[index]+=changeNum
        return
    mid = (start+end)//2
    update(start,mid,index*2,left,right,changeNum)
    update(mid+1,end,index*2+1,left,right,changeNum)
    tree[index]=tree[index*2]+tree[index*2+1]
    
def query(start,end,index,left,right):
    if left>end or right<start:
        return 0
    if left<=start and end<=right:
        return tree[index]
    mid = (start+end)//2
    return query(start,mid,index*2,left,right)+query(mid+1,end,index*2+1,left,right)

def init(start,end,index):
    if start==end:
        tree[index] = nodes[start]
        return tree[index]
    mid = (start+end)//2
    tree[index] = init(start,mid,index*2)+init(mid+1,end,index*2+1)
    return tree[index]

if __name__ == "__main__":    
    #노드수, 수의변경, 구간합
    n,m,k = map(int,input().rstrip().split())
    tree = [0]*(n*4)
    for _ in range(n):
        nodes.append(int(input()))
    init(0,n-1,1)
    for _ in range(m+k):
        msg = list(map(int,input().rstrip().split()))
        if len(msg)==3:#
            a,b,c = msg
        else:
            a,b,c,d = msg
        
        if a==1:#b부터 c까지 d를 더하라
            for i in range(b,c+1):
                nodes[i]+=d
            update(0,n-1,1,b-1,c-1,d)
        else:#b부터 c까지의 합을 출력하라
            print(query(0,n-1,1,b-1,c-1))