def factorial(n):
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)

n,k=map(int,input().split())
if 0<=k and k<=n:
    print(round(factorial(n)/(factorial(k)*factorial(n-k))))
else:
    print(0)
