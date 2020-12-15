import sys
input = sys.stdin.readline

tree= list()
nodes = list()

def update(start,end,index,cidx,cnum):
    if cidx < start or end < cidx: return    
    if start==end:  
        #끝에 도달하면서 값을 수정해야함
        tree[index] = nodes[cidx]
        return    
    mid = (start+end)//2
    update(start,mid,index*2,cidx,cnum)
    update(mid+1,end,index*2+1,cidx,cnum)
    tree[index] = min(tree[index*2],tree[index*2+1])

def query(start,end,index,left,right):
    if left>end or right<start:
        return 10**9+1
    if left <=start and end <= right:
        return tree[index]
    mid = (start+end)//2
    return  min(query(start,mid,index*2,left,right),query(mid+1,end,index*2+1,left,right))

def init(start,end,index):
    if start==end:
        tree[index] = nodes[start]
        return tree[index]
    mid = (start+end)//2
    tree[index] = min(init(start,mid,index*2),init(mid+1,end,index*2+1))
    return tree[index]

if __name__ == "__main__":
    n = int(input())
    tree = [0]*(n*4)
    nodes = list(map(int,input().rstrip().split()))
    m = int(input())
    init(0,n-1,1)
    for _ in range(m):
        # 1:update, 2:min
        a,b,c = map(int,input().rstrip().split())
        if a==2:#sum
            if b>c:#범위가 반전되는 경우
                b,c=c,b
            print(query(0,n-1,1,b-1,c-1))
        elif a==1:#update     
            nodes[b-1]=c
            update(0,n-1,1,b-1,c)