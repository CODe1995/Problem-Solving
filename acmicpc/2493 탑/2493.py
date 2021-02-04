import sys
N = int(input())
arr = [0]+list(map(int,input().split()))
stack = list()
answer = [0]*(N+1)
for i in range(N,0,-1):
    while len(stack)>0 and arr[stack[-1]]<arr[i]:
        answer[stack.pop()]+=i
    stack.append(i)
for i in range(1,N+1):
    sys.stdout.write(str(answer[i])+" ")