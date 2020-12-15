import sys
input = sys.stdin.readline

tree= list()
tree_idx = list()
nodes = list()

#min 함수 재정의
def min(a,b):
    if a[0]>b[0]:return b
    elif a[0]<b[0]:return a
    else:#같은경우 index로 비교
        if a[1]<b[1]:return a
        else: return b    
def update(start,end,index,cidx,diff):
    if cidx < start or end < cidx: return       
    if start==end:
        # nodes[cidx]=diff
        tree[index]=diff
        return 
    mid = (start+end)//2
    update(start,mid,index*2,cidx,diff)
    update(mid+1,end,index*2+1,cidx,diff)
    tree[index],tree_idx[index] = min((tree[index*2],tree_idx[index*2]),(tree[index*2+1],tree_idx[index*2+1]))

def query(start,end,index,left,right):
    if left>end or right<start:
        return 0,-1
    if left <=start and end <= right:
        return tree[index],tree_idx[index]
    mid = (start+end)//2
    return  min(query(start,mid,index*2,left,right),query(mid+1,end,index*2+1,left,right))

def init(start,end,index):
    if start==end:
        tree[index],tree_idx[index] = nodes[start],start
        return tree[index],tree_idx[index]
    mid = (start+end)//2
    tree[index],tree_idx[index] = min(init(start,mid,index*2),init(mid+1,end,index*2+1))
    return tree[index],tree_idx[index]

if __name__ == "__main__":
    #크기가 가장 작은 값의 index
    n = int(input())
    tree = [0]*(n*4)
    tree_idx = [i for i in range(n*4)]  #index도 함께 저장
    nodes = list(map(int,input().rstrip().split()))

    m = int(input())
    init(0,n-1,1)
    for _ in range(m):
        lst = input().rstrip().split()
        if len(lst)==1:
            print(tree_idx[1]+1)
        else:#변경
            a,b,c = map(int,lst)
            # diff = c - nodes[b-1]
            nodes[b-1]=c
            update(0,n-1,1,b-1,c)