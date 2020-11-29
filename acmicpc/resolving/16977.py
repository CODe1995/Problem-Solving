import sys
input = sys.stdin.readline

n = int(input())
graph = [0]*(n+2)
graph[1:n+1] = list(map(int,input().rstrip().split()))

q = int(input())
#l번째 직사각형부터 r번째 직사각형까지만 있을 때, 
# 너비가 w이면서 가장 넓이가 큰 직사각형의 높이를 출력
for _ in range(q):
    l,r,w = map(int,input().rstrip().split())
    # tmpArray = [0]*(r-l+3)
    tmpArray = [0] + graph[l:r+1] + [0]

    stack = []
    maxheight = 0
    stack.append(0)
    for i in range(1,r-l+3):
        while stack and tmpArray[stack[-1]]>tmpArray[i]:
            height = tmpArray[stack[-1]]
            stack.pop()
            width = i - stack[-1] -1
            if width>=w:
                maxheight = max(maxheight, height)                    
        stack.append(i)
    print(maxheight)