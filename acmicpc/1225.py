#런타임에러 -> split으로 받기
#시간초과 -> 반복문 두개 X O(n)으로 인수분해 사용하기
A,B= input().split()
result = 0
insu = 0
for anum in range(0,len(A)):
    result += int(A[anum])
for bnum in range(0,len(B)):
    insu += int(B[bnum])

print(result*insu)