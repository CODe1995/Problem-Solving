import sys
input = sys.stdin.readline
def ii():return int(input())
def mii():return map(int,input().rstrip().split())
def lmii():return list(map(int,input().rstrip().split()))
tree= list()
nodes = list()
n,q,u,v = mii()
nodes = lmii()
tree = [0]*(n*4)
def update(start,end,index,cidx,diff):
    if index>end or index<start:return#범위밖
    tree[index]+=diff
    if start==end:return
    mid = (start+end)//2
    update(start,mid,index*2,cidx,diff)
    update(mid+1,end,index*2+1,cidx,diff)
    
def query(start,end,index,left,right):
    if left>end or right < start:#범위밖
        return 0
    if left<=start and end<=right:#범위내
        return u*tree[index]+v*(end-start)
    mid = (start+end)//2
    res = query(start,mid,index*2,left,right)+query(mid+1,end,index*2+1,left,right)
    return res

def init(start,end,index):
    if start==end:
        tree[index] = nodes[start]
        return tree[index]
    mid = (start+end)//2    
    tree[index] = init(start,mid,index*2)+init(mid+1,end,index*2+1)
    return tree[index]

init(0,n-1,1)
for _ in range(q):
    c,a,b = mii()
    if c == 0:#첫번째쿼리 max
        res = query(0,n-1,1,a-1,b-1)
        print(res)
    else:#두번재 쿼리 update
        diff = b-nodes[a-1]
        nodes[a-1]=b
        update(0,n-1,1,a-1,diff)
        print('update: ',tree)
