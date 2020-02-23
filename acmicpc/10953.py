import sys
T = int(input())
inp = sys.stdin.readline
for i in range(T):
    data = list(map(int,inp().split(',')))
    print(data[0]+data[1])