import sys
input = sys.stdin.readline

T = int(input().rstrip())
for _ in range(T):
    a,b = map(int,input().rstrip().split())
    b = int(str(b)[-1])
    tmp = int(str(a**b)[-1] )
    print(10 if tmp==0 else tmp)