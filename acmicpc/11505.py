import sys
from math import log,ceil
input = sys.stdin.readline

tree = list()
nodes = list()

#ChangeIdx : 수정할 인덱스, ChangeNum : 수정할 숫자
def update(start, end, index, ChangeIdx, ChangeNum):
    #범위를 벗어나는 경우
    if ChangeIdx<start or ChangeIdx>end:return
    if start==end:#끝지점 도달하면 노드 변경
        tree[index] = ChangeNum
        return    
    mid = (start+end)//2
    update(start,mid,index*2,ChangeIdx,ChangeNum)
    update(mid+1,end,index*2+1,ChangeIdx,ChangeNum)
    
    #하나씩 내려가면서 다른 원소들도 갱신해야함.    
    tree[index] = (tree[index*2]*tree[index*2+1])%1000000007
    

#곱을 출력하는 함수
def query(start,end,index,left,right):
    # 입력된 쿼리의 범위가 트리의 범위를 벗어나는 경우
    if left>end or right<start:
        return 1    #곱이므로 1로 반환
    #범위 내인 경우
    if start>=left and end<=right:
        return tree[index]%1000000007
    mid = (start+end)//2
    return (query(start,mid,index*2,left,right)*query(mid+1,end,index*2+1,left,right))%1000000007
#누적 곱으로 트리 구성해줌
def init(start,end,index):
    if start==end:
        tree[index] = nodes[start]
        return tree[index]
    mid = (start+end)//2
    tree[index] = (init(start,mid,index*2)*init(mid+1,end,index*2+1))%1000000007
    return tree[index]

if __name__ == "__main__":
    #노드수, 수의변경 수, 구간합 수
    n,m,k = map(int,input().rstrip().split())
    for _ in range(n):
        nodes.append(int(input()))
    tree = [0]*(n*4)
    init(0,n-1,1)
    for _ in range(m+k):
        a,b,c = map(int,input().rstrip().split())        
        # a==1 : b번째 수를 c로 변경
        # a==2 : b부터 c까지 곱을 출력
        if(a==1):
            update(0,n-1,1,b-1,c)
            # print(tree,'\n',nodes)
        else:
            print("%d"%query(0,n-1,1,b-1,c-1))