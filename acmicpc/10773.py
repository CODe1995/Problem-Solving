import sys
inp = sys.stdin.readline
K=int(input())
stk = []
for i in range(K):
    data = int(inp())
    if data == 0:
        stk.pop()
    else:
        stk.append(data)
print(sum(stk))