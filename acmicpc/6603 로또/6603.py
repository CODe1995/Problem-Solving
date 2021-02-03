#21.02.03 10:21
import sys
input = sys.stdin.readline
flag = []
arr = []
N = 0
def solve(start,depth):
    if depth==6:
        for x in flag:
            print(x,end=' ')
        print()
        return
    for i in range(start,len(arr)):
        flag[depth]=arr[i]
        solve(i+1,depth+1)
while True:
    arr = list(map(int,input().strip().split()))
    if len(arr)==1:break
    del arr[0]
    flag = [0]*6
    solve(0,0)
    print()