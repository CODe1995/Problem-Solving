import sys
input = sys.stdin.readline
N = int(input())
arr = list()
stack = list()
answer = [0]*N
for _ in range(N):
    arr.append(int(input()))
for i in range(N-1,-1,-1):
    while len(stack)>0 and arr[stack[-1]]<arr[i]:
        answer[i]+=answer[stack.pop()]+1
    stack.append(i)
print(sum(answer))