import sys
input = sys.stdin.readline
#펜 윅 트리, Binary indexded Tree
tree= list() 
nodes = list()

def answer(start,end,index,left,right):
    if left>end or start<right:return 0
    if left<=start and end<=right:return tree[index]
    mid = (start+end)//2
    return answer(start,mid,index*2,left,right)+answer(mid+1,end,index*2+1,left,right)

def update(node):
    while node>0:
        tree[node]+=1
        node//=2

if __name__ == "__main__":
    n = int(input())
    tree = [0]*(n*4)
    s=1
    ans=0
    #첫번째 인덱스 위치 찾기
    while s<n:s*=2
    nodes = list(map(int,input().rstrip().split()))
    for i in nodes:
        res = answer(1,s,1,i+1,s)
        ans += res
        update(i)