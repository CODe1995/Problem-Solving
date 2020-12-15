import sys
input = sys.stdin.readline
n,m = map(int,input().rstrip().split())
nName=[]
mName=[]
for _ in range(n):
    nName.append(input().rstrip())
for _ in range(m):
    mName.append(input().rstrip())

nName.sort()
mName.sort()
answer = []
for i in range(n):
    sPnt = 0
    ePnt = m-1
    while sPnt<=ePnt:
        mid = (ePnt+sPnt) //2
        if mName[mid]==nName[i]:
            answer.append(nName[i])
            break
        elif mName[mid]>nName[i]:
            ePnt = mid-1
        else:
            sPnt = mid+1
print(len(answer))
for i in answer:
    print(i)