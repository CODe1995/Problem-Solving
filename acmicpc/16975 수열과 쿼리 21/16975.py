
import sys,math
input = sys.stdin.readline
tree = list()
lazy = list()
nodes = list()

def init(start,end,index):
    if start==end:
        tree[index] = nodes[start]
        return tree[index]
    mid = start+end >>1
    tree[index]=init(start,mid,index*2)+init(mid+1,end,index*2+1)
    return tree[index]

def lazy_update(start,end,index):
    if lazy[index]:
        if start!=end:
            lazy[index*2]+=lazy[index]
            lazy[index*2+1]+=lazy[index]
        tree[index]+=lazy[index]*(end-start+1)
        lazy[index]=0
    return

#left-right 전체범위, qs-qe 쿼리 범위
def query(left,right,index,qs,qe):
    lazy_update(left,right,index)
    if left>qe or right<qs:return 0
    if qs <= left and  qe >= right:return tree[index]
    mid = left+right >>1
    return query(left,mid,index*2,qs,qe)+query(mid+1,right,index*2+1,qs,qe)

def update(left,right,index,qs,qe,diff):
    lazy_update(left,right,index)
    if left>qe or right<qs:return
    if qs <= left and  qe >= right:
        lazy[index]=diff
        lazy_update(left,right,index)
        return
    mid = left+right >>1
    update(left,mid,index*2,qs,qe,diff)
    update(mid+1,right,index*2+1,qs,qe,diff)
    tree[index]=tree[index*2]+tree[index*2+1]
    
if __name__=="__main__":
    N = int(input())
    nodes = [0]+list(map(int,input().split()))
    M = int(input())
    tree = [0]*(N*4)
    lazy = [0]*(N*4)
    init(1,N,1)
    # print(tree)
    for _ in range(M):
        msg = list(map(int,input().split()))
        if msg[0]==1:
            update(1,N,1,msg[1],msg[2],msg[3])
        else:
            print(query(1,N,1,msg[1],msg[1]))