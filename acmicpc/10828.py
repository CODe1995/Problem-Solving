import sys
input = sys.stdin.readline
stack = []

for i in range(int(input())):
    tri = input().rstrip()
    if tri.split()[0] == "push":
        stack.append(tri.split()[1])
    elif tri == "pop":
        if not stack:
            print("-1")
        else:
            print(stack[-1])
            stack.pop()
    elif tri == "size":
        print(len(stack))
    elif tri == "empty":
        if not stack:
            print("1")
        else:
            print("0")
    elif tri == "top":
        if not stack:
            print("-1")
        else:
            print(stack[-1])