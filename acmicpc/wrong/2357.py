#2020.12.14
import sys, math
input = sys.stdin.readline
tree = list()#세그먼트 트리 들어가는 변수
nodes = list()  #노드 들어가는 변수

#start,end = 구간을 합하고자 하는 범위
def pSum(start, end, node, left, right):
    #범위 밖
    if left>end or right<start: return 0
    #범위 내
    if left<=start and end<=right: return tree[node]
    #둘 다 아닌 경우
    mid = (start+end)/2
    return pSum(start,mid,node*2,left,right)+pSum(mid+1,end,node*2+1,left,right)

def init(start, end, index):
    if start==end:
        tree[index] = nodes[start]
        return tree[index]
    mid = (start+end) //2
    #좌측 + 우측
    tree[index] = init(start,mid,index*2) + init(mid+1,end,index*2+1)
    return tree[index]
    
if __name__ == "__main__":
    #n:노드 수, m:쿼리 수
    n,m = map(int,input().rstrip().split())
    #필요한 노드만큼 트리 초기화
    # tree = [0]*(pow(2,math.ceil(math.log(m,2))+1)-1)
    tree = [0]*(n*4)    #모든 범위 커버 가능
    
    for _ in range(n):
        nodes.append(int(input()))
    
    for i in range(m):
        a,b = map(int,input().rstrip().split())
        

    init(0,n-1,0)
    print(tree)