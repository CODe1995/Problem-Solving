import sys
input = sys.stdin.readline
tree = list()
nodes = list()

def update(start,end,index,changeIdx,changeNum):
    if index<start or end<index:return
    tree[index]+=changeNum-nodes[changeIdx]
    if start==end:return
    mid = (start+end)//2
    update(start,mid,index*2,changeIdx,changeNum)
    update(mid+1,end,index*2+1,changeIdx,changeNum)
    
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
    n,q = map(int,input().rstrip().split())
    tree = [0]*(n*4)
    nodes = list(map(int,input().rstrip().split()))
    init(0,n-1,1)
    for _ in range(q):
        # x~y까지 합을 출력하라
        # a번째 수를 b로 바꿔라
        x,y,a,b = map(int,input().rstrip().split())
        print(query(0,n-1,1,x-1,y-1))
        update(0,n-1,1,a-1,b)