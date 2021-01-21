import math
MAXINT = 1000001
n = int(input())
arr = [False,False]+[True]*(MAXINT-2)
for i in range(2,MAXINT):
    if arr[i]==False:continue
    for j in range(2*i,MAXINT,i):
        arr[j]=False
answer = 0
for i in range(n,MAXINT):
    if arr[i]==True:
        tmp = str(i)
        if tmp[:len(tmp)//2]==tmp[::-1][:len(tmp)//2]:
            answer= i
            break
if answer ==0:
    answer= 1003001
print(answer)