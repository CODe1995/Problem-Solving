# https://hillier.tistory.com/105
import sys
input = sys.stdin.readline
N, C = map(int, input().strip().split())
M = int(input())
arr = [list(map(int,input().split())) for _ in range(M)]
arr.sort(key=lambda x:x[1])
boxes = [C] * (N+1)
answer = 0
for start, end, box in arr:
    _min = C
    for i in range(start, end):
        _min = min(_min, boxes[i])
    _min = min(_min, box)
    for i in range(start, end):
        boxes[i] -= _min
    answer += _min
print(answer)