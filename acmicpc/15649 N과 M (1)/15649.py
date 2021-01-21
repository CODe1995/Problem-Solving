from itertools import combinations, permutations
n,m = map(int,input().split())
arr = [str(i) for i in range(1,n+1)]
pmt = permutations(arr,m)

for c in pmt:
    print(' '.join(c))    