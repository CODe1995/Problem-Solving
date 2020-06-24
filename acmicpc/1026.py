import sys
input = sys.stdin.readline

n = int(input().rstrip())
arrA = list(map(int,input().split()))
arrB = list(map(int,input().split()))

arrA.sort()
arrB.sort(reverse=True)
su = 0
for i in range(n):
    su += arrA[i]*arrB[i]
print(su)
