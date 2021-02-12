import sys
input = sys.stdin.readline
N,T,Q = map(int,input().split())
tree = [0]*(N*4)
lazy = [0]*(N*4)
nodes = [1]*N

def lazy_update(start,end,index):
    if lazy[index]!=0:
        if start!=end:
            lazy[index*2] = lazy[index]
            lazy[index*2+1] = lazy[index]        
        tree[index] = lazy[index]
        lazy[index] = 0
    
def update(start,end,index,qs,qe,color):
    lazy_update(start,end,index)
    if qs > end or qe < start:return
    if qs <= start and end <= qe:
        lazy[index] = color
        lazy_update(start,end,index)
        return
    mid = start+end>>1
    update(start,mid,index*2,qs,qe,color)
    update(mid+1,end,index*2+1,qs,qe,color)
    tree[index] = tree[index*2] | tree[index*2+1]
    
def init(start,end,index):
    if start==end:
        tree[index] = nodes[start]
        return tree[index]
    mid = start+end >>1
    tree[index] = init(start,mid,index*2) | init(mid+1,end,index*2+1)
    return tree[index]
def query(start,end,index,qs,qe):
    lazy_update(start,end,index)
    if qs>end or qe<start:return 0
    if qs<=start and end<=qe:
        return tree[index]
    mid = start+end>>1
    return query(start,mid,index*2,qs,qe)|query(mid+1,end,index*2+1,qs,qe)

#Seg
init(0,N-1,1)
for _ in range(Q):
    tmp = list(input().split())
    t2 = list(map(int,[tmp[1],tmp[2]]))
    a = min(t2)
    b = max(t2)
    if tmp[0]=='C':
        c = int(tmp[3])
        c= 1<<(c-1)#컬러 비트마스킹으로 넘김
        update(0,N-1,1,a-1,b-1,c)
    else:
        ans = query(0,N-1,1,a-1,b-1)
        cnt = 0
        while ans:
            if ans&1:cnt+=1
            ans>>=1
        print(cnt)