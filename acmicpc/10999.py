import sys,math
input = sys.stdin.readline
tree = list()
nodes = list()

def propagate(start,end,index):
    if lazy[index]:
        if start!=end:
            lazy[index*2]+=lazy[index]
            lazy[index*2+1]+=lazy[index]
        tree[index]+=lazy[index]*(end-start+1)
        lazy[index]=0
    return

def update(start,end,index,left,right,changeNum):
    propagate(start,end,index)
    if left>end or right<start:return
    if start==end:
        lazy[index]=changeNum
        propagate(start,end,index)
        # tree[index]+=changeNum
        return
    mid = (start+end)//2
    update(start,mid,index*2,left,right,changeNum)
    update(mid+1,end,index*2+1,left,right,changeNum)
    tree[index]=tree[index*2]+tree[index*2+1]
    
def query(start,end,index,left,right):
    propagate(start,end,index)
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
    n,m,k = map(int,input().split())
    height = math.ceil(math.log2(n))
    size = 2**(height+1)
    tree = [0]*size
    lazy = [0]*size    
    for _ in range(n):nodes.append(int(input()))
    init(0,n-1,1)
    for _ in range(m+k):
        msg = list(map(int,input().split()))
        if msg[0]==1:#b부터 c까지 d를 더하라
            update(0,n-1,1,msg[1]-1,msg[2]-1,msg[3])
        else:#b부터 c까지의 합을 출력하라
            sys.stdout.write(str(query(0,n-1,1,msg[1]-1,msg[2]-1)))