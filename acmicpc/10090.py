import sys
input = sys.stdin.readline
def ii():return int(input())
def mii():return map(int,input().rstrip().split())
def lmii():return list(map(int,input().rstrip().split()))
#펜 윅 트리, Binary indexded Tree
n=0
arr = list()
fenwick = list()

def query(index):
    ret=0
    while index>0:
        ret+=fenwick[index]
        index-=index&-index
    return ret
def update(index):
    while index<=n:
        fenwick[index]+=1
        index+=index&-index

n = ii()
arr = [0]*n
fenwick = [0]*(n+1)
tmp = lmii()
for idx,num in enumerate(tmp):
    arr[idx]=[num,idx]
arr.sort()
ans = 0
for a,b in arr:
    # ans += query(n)-query(b)#index
    qn,qb =query(n),query(b) 
    ans += qn-qb
    print("query({})={}, query({})={}".format(n,qn,b,qb))
    update(b+1)
print(ans)