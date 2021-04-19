import sys
from functools import cmp_to_key
input = sys.stdin.readline
def ccw(p1,p2,p3):
    return p1[0]*(p2[1]-p3[1]) + p2[0]*(p3[1]-p1[1]) + p3[0]*(p1[1]-p2[1])
def compare(a,b):
    resA = a[2]*b[3]
    resB = a[3]*b[2]
    if resA > resB:
        return -1
    elif resA==resB:
        return 0
    return 1
    
N = int(input())
arr = list()
for i in range(N):
    a,b = map(int,input().split())
    arr.append([a,b,1,0])#x,y,p,q
arr = sorted(arr,key=lambda x:[x[1],x[0]])

for i in range(1,N):
    arr[i][2] = arr[i][0] - arr[0][0]
    arr[i][3] = arr[i][1] - arr[0][1]

arr = [arr[0]]+sorted(arr[1:],key=cmp_to_key(compare))
# print(arr)
stack = list()
stack.append(0)
stack.append(1)
next = 2

while next<N:
    while len(stack)>=2:
        second = stack.pop()
        first = stack[-1]
        if ccw(arr[first],arr[second],arr[next])>0:
            stack.append(second)
            break
    stack.append(next)
    next+=1

print(len(stack))
