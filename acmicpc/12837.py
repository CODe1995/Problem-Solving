import sys
input = sys.stdin.readline

tree= list()
nodes = list()

def update(start,end,index,cidx,diff):
    if cidx < start or end < cidx: return       
    #계속 값을 수정해야함
    tree[index] += diff
    if start==end:return 
    mid = (start+end)//2
    update(start,mid,index*2,cidx,diff)
    update(mid+1,end,index*2+1,cidx,diff)

def query(start,end,index,left,right):
    if left>end or right<start:
        return 0
    if left <=start and end <= right:
        return tree[index]
    mid = (start+end)//2
    return  query(start,mid,index*2,left,right)+query(mid+1,end,index*2+1,left,right)

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
    nodes = [0]*n
    init(0,n-1,1)
    for _ in range(q):
        a,b,c = map(int,input().rstrip().split())
        if a==2:#출력
            if b>c:#범위가 반전되는 경우
                b,c=c,b
            print(query(0,n-1,1,b-1,c-1))
        elif a==1:#추가
            diff = c - nodes[b-1]   #차이
            nodes[b-1]=c
            update(0,n-1,1,b-1,diff)