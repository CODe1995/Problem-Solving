import sys
from collections import Counter
inp = sys.stdin.readline
N= int(input())
data = []
for i in range(N):
    data.append(int(inp().rstrip()))
print(round(sum(data)/len(data)))   #산술평균
print(sorted(data)[(len(data)-1)//2])   #중앙값

cnt = Counter(data)
cnt = sorted(cnt.items(),key=lambda min: (-min[1],min[0]))
if len(cnt) > 1 and cnt[0][1] == cnt[1][1]:
    print(cnt[1][0])
else:
    print(cnt[0][0])

print(max(data)-min(data))  #최댓값과 최솟값의 차이