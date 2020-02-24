import sys
inp = sys.stdin.readline
N,K=map(int,inp().split())
datas = list(map(int,inp().split()))
print(sorted(datas)[K-1])