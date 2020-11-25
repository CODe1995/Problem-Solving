import sys
input = sys.stdin.readline

N,M = map(int,input().rstrip().split())   #집합 개수, 검사 개수
dictionary = {input().rstrip() for _ in range(N)}
cnt = 0
for i in range(M):
    tmp = input().rstrip()
    if tmp in dictionary:
        cnt+=1
print(cnt)