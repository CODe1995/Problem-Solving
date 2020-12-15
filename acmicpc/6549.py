import sys
input = sys.stdin.readline

while True:
    lst = list(map(int,input().rstrip().split()))
    if len(lst)==1: break
    n = lst[0]

    graph = [0]*(n+2)
    for i in range(1,n+1):
        graph[i] = lst[i]
    stack = []
    maxwidth = 0
    stack.append(0)
    for i in range(1,n+2):
        while stack and graph[stack[-1]]>graph[i]:
            height = graph[stack[-1]]
            stack.pop()
            width = i - stack[-1] -1
            maxwidth = max(maxwidth, width*height)
        stack.append(i)

    print(maxwidth)