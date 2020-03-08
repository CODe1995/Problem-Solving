N = int(input())
A = list(map(int,input().split()))
sumA=[]
#Prefix Sum Algorithm
for i in range(N):
    if i==0:sumA=A
    else:sumA[i]=sumA[i-1]+sumA[i]
print(sumA)
M = int(input())
for i in range(1,M+1):
    cnt = 0
    qi,qj = map(int,input().split())
    tmpA = A[qi-1:qj]

