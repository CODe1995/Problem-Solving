##########################################################
import sys
input = sys.stdin.readline
def ii():return int(input())
def mii():return map(int,input().rstrip().split())
def lmii():return list(map(int,input().rstrip().split()))
##########################################################
from math import ceil,log2
MAXNUM = 1e9
nodes = list()
n,q,u,v = mii()
nodes = [0]+lmii()
ncnt = n*4
tree=[{
    'ls' :-MAXNUM,#왼쪽 구간 최대합
    'rs' : -MAXNUM,#우측 구간 최대합
    'lrs' : -MAXNUM,#구간 전체(좌+우) 최대합
    'mxs' : 0#좌측,우측,전체 최대합 중의 최대
}]*ncnt
#노드 두개를 연산함
def calc(L,R):
    tmp={
            'ls' : max(L['ls'],L['lrs']+R['ls']),
            'rs' : max(R['rs'],L['rs']+R['lrs']),
            'lrs' : L['lrs']+R['lrs'],
            'mxs' : max(L['mxs'],R['mxs'],L['rs']+R['ls']),
            }
    return tmp
    
def query(start,end,index,left,right):
    if left>end or right < start:#범위밖
        tmp={
            'ls' :-MAXNUM,#왼쪽 구간 최대합
            'rs' : -MAXNUM,#우측 구간 최대합
            'lrs' : 0,#구간 전체(좌+우) 최대합
            'mxs' : -MAXNUM#좌측,우측,전체 최대합 중의 최대
        }
        return tmp 
    if left<=start and end<=right:#범위내
        return tree[index]
    mid = (start+end)//2
    r1,r2 = query(start,mid,index*2,left,right), query(mid+1,end,index*2+1,left,right)    
    return calc(r1,r2)

#시작점, 끝점, 현재위치, 수정좌표위치, 수정될값
def update(start,end,index,cidx,cnum):#init과 동일
    if cidx>end or cidx<start:return tree[index]
    if start==end:
        tree[index]={'ls' : cnum, 'rs' : cnum, 'lrs' : cnum, 'mxs' : cnum}        
        return tree[index]
    mid = (start+end)//2        
    r1=update(start,mid,index*2,cidx,cnum)
    r2=update(mid+1,end,index*2+1,cidx,cnum)
    tree[index] = calc(r1,r2)
    return tree[index]

def printTree():    
    print('============Tree===========')
    for i in tree:
        print(i)

for i in range(1,n+1):#u와 v의 값이 반영된 쿼리 업데이트(init)
    # print("init_updates(%d,%d,%d,%d,%d)"%(0,n-1,i,1,u*nodes[i]+v))
    update(1,n,1,i,u*nodes[i]+v)
    # printTree()

# for i in range(0,ncnt):
#     print(tree[i])

for _ in range(q):
    c,a,b = mii()
    if c == 0:#첫번째쿼리 max
        print(query(1,n,1,a,b)['mxs']-v)
    else:#두번재 쿼리 update
        nodes[a]=b
        update(1,n,1,a,u*b+v)
        # printTree()
