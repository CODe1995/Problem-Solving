n = int(input())
arr = []
while n:
    n-=1
    arr.append(int(input()))
for i in sorted(arr):
    print(i)