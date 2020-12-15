data = list(map(int,input().split()))
res =0
for i in data:
    res += i**2
print(res%10)