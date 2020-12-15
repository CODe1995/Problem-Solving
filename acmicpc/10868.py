#2020.12.14
import sys
from math import log,ceil
input = sys.stdin.readline
tree = list()#세그먼트 트리 들어가는 변수
nodes = list()  #노드 들어가는 변수

#start,end = 구간 시작-끝
def query(start, end, index, left, right):
    #범위 밖
    if left>end or right<start: return 1000000001
    #범위 내
    if left<=start and end<=right: return tree[index]
    #둘 다 아닌 경우
    mid = (start+end)//2
    return min(query(start,mid,index*2,left,right),query(mid+1,end,index*2+1,left,right))

def init(start, end, index):
    if start==end:
        tree[index] = nodes[start]
        return tree[index]
    mid = (start+end) //2
    #좌측 + 우측
    tree[index] = min(init(start,mid,index*2), init(mid+1,end,index*2+1))
    return tree[index]
    
if __name__ == "__main__":
    #n:노드 수, m:쿼리 수
    n,m = map(int,input().rstrip().split())
    #필요한 노드만큼 트리 초기화
    tree = [0]*(n*4)    #모든 범위 커버 가능
    
    for _ in range(n):
        nodes.append(int(input()))
    
    init(0,n-1,1)
    for i in range(m):
        a,b = map(int,input().rstrip().split())
        print(query(0,n-1,1,a-1,b-1))