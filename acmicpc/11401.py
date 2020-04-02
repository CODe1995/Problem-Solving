#math.factorial은 시간초과, 그래서 factorial을 dp로 풀자
#dp문제가 아니라 페르마의소정리, 확장유클리드호제법으로 풀어야한다

import math
    
n,k=map(int,input().split())
res = 0
if 0<=k and k<=n:
    res = factorial(n)/(factorial(k)*factorial(n-k))
else:
    res = 0
print(int(res%1000000007))
