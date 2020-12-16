import sys
input = sys.stdin.readline
def ii():return int(input())
def mii():return map(int,input().rstrip().split())
def lmii():return list(map(int,input().rstrip().split()))

arr = list()
tree = list()
N=0
def query(index):    
    ret = 0
    while index:        
        ret += tree[index]
        # index &= (index-1)
        index -= (index&-index)
    return ret
def update(index):
    while index<=N:
        tree[index]+=1        
        index+=(index&-index)
if __name__ == "__main__":
    N = ii()
    arr = lmii()#원본 배열
    tree = [0]*(N+1)

    for i,num in enumerate(arr):
        arr[i] = [num,i]
    print(arr)
    #index 역순으로 정렬
    arr=sorted(arr,key=lambda x:x[1],reverse=True)
    print(arr)
    ans = 0
    for i in range(N):
        ans+=query(arr[i][0]-1)
        update(arr[i][0])
    print(ans)
