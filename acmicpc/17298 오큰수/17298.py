import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int,input().rstrip().split()))
answer = [-1]*N
stack = list()
def solve():
    for i in range(len(arr)):
        while(len(stack)>0 and arr[stack[-1]]<arr[i]):
            answer[stack.pop()] = arr[i]
        stack.append(i)
if __name__=="__main__":
    solve()
    for i in answer:
        sys.stdout.write(str(i)+' ')