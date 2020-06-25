import sys
input = sys.stdin.readline
N, L = map(int,input().split())
ansarr = []
arrsum = 0
def fibo(num):
    if num<2:
        return num
    else:
        return num+fibo(num-1)

while L<=100:
    x = (N-fibo(L))/L
    y = (N-fibo(L))%L
    if y == 0 and x>=-1:
        for ans in range(1,L+1):
            print(int(x+ans), end = ' ')
        break
    else:
        L+=1
if L>100:print(-1) 