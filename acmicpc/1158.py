N,K=map(int,input().split())
lists = list(range(1,N+1))
while len(lists)>0:
    print(lists[K-1])
    del lists[K-1]