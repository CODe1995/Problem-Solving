##########################################################
import sys
input = sys.stdin.readline
def ii():return int(input())
def mii():return map(int,input().rstrip().split())
def lmii():return list(map(int,input().rstrip().split()))
##########################################################

n = ii()
tree = list()
for _ in range(n):
    tree.append(lmii())
tree.sort()
tree = sorted(tree,key=lambda x: x[1])
# print(tree)
# sys.exit()
prev= tree[0][1]
ans = 1
for a,b in tree[1:]:
    if a>=prev:
        ans+=1
        prev=b
print(ans)