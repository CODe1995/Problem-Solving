import sys
input = sys.stdin.readline
def ii():return int(input())
def mii():return map(int,input().rstrip().split())
def lmii():return list(map(int,input().rstrip().split()))

N=0
arr = list()
fenwick = list()
#fenwick을 이용해 값을 구하는 함수
def query(index):
    # print('[Query] index({}) fenwick : {}'.format(index,fenwick))
    ret = 0
    while index>0:
        ret+=fenwick[index]
        index -= index&-index
    # print('[Query] fenwick : {}, ret : {}'.format(fenwick,ret))
    return ret
def update(index):
    # print('[Update] index(%d) before update :'%(index),fenwick)
    while index<=N:
        fenwick[index]+=1
        index += index&-index
    # print('[Update] index(%d) after update :'%(index),fenwick)

if __name__ == "__main__":
    N = ii()
    arr= [0]*N
    fenwick = [0]*(N+1)
    tmp = lmii()#원본 배열
    for idx,num in enumerate(tmp):
        arr[idx] = [num,idx]
    # for i in arr:
    #     print(i)
    arr.sort()
    ans = 0
    for a,b in arr:
        # print("Query({})".format(b))
        ans += query(N)-query(b)
        # print("Update({})".format(b+1))
        update(b+1)
    print(ans)
