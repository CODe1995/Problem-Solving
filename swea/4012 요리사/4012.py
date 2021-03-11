from itertools import combinations
import sys
input = sys.stdin.readline
T = int(input())
for t in range(1,T+1):
    N = int(input())
    field = [list(map(int,input().strip().split())) for _ in range(N)]
    
    cmb = list(combinations(range(N),2))
    for c in cmb:
        print(c)
    print('====')
    for g1 in combinations(range(N), N//2):
        g2 = [i for i in range(N) if i not in g1]
        print(g1,g2)