s = input()
t = input()

stack = []
for c in s:
    stack.append(c)
    if len(stack)>=len(t):
        if ''.join(stack[len(stack)-len(t):])==t:
            for i in range(len(t)):
                stack.pop()
if stack:
    print(''.join(stack))
else:
    print('FRULA')