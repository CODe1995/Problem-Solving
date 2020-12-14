#2020.12.14
import sys
from math import log,ceil
input = sys.stdin.readline
min_tree = list()
max_tree = list()
nodes = list()  #노드 들어가는 변수

#start,end = 구간 시작-끝
def min_query(start, end, index, left, right):
    #범위 밖
    if left>end or right<start: return 1000000001
    #범위 내
    if left<=start and end<=right: return min_tree[index]
    #둘 다 아닌 경우
    mid = (start+end)//2
    return min(min_query(start,mid,index*2,left,right),min_query(mid+1,end,index*2+1,left,right))
def max_query(start, end, index, left, right):
    #범위 밖
    if left>end or right<start: return 0
    #범위 내
    if left<=start and end<=right: return max_tree[index]
    #둘 다 아닌 경우
    mid = (start+end)//2
    return max(max_query(start,mid,index*2,left,right),max_query(mid+1,end,index*2+1,left,right))

def min_init(start, end, index):
    if start==end:
        min_tree[index] = nodes[start]
        return min_tree[index]
    mid = (start+end) //2
    #좌측 + 우측
    min_tree[index] = min(min_init(start,mid,index*2), min_init(mid+1,end,index*2+1))
    return min_tree[index]

def max_init(start, end, index):
    if start==end:
        max_tree[index] = nodes[start]
        return max_tree[index]
    mid = (start+end) //2
    max_tree[index] = max(max_init(start,mid,index*2), max_init(mid+1,end,index*2+1))
    return max_tree[index]

if __name__ == "__main__":
    #n:노드 수, m:쿼리 수
    n,m = map(int,input().rstrip().split())
    #필요한 노드만큼 트리 초기화
    min_tree = [0]*(n*4)    #모든 범위 커버 가능
    max_tree = [0]*(n*4)
    
    for _ in range(n):
        nodes.append(int(input()))
    
    min_init(0,n-1,1)
    max_init(0,n-1,1)

    for i in range(m):
        a,b = map(int,input().rstrip().split())
        print(min_query(0,n-1,1,a-1,b-1), max_query(0,n-1,1,a-1,b-1))