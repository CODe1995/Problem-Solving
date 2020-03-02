def fibonacci(n):
    if len(cn)<=n:
        for i in range(len(cn),n+1):
            cn.append([cn[i-1][0]+cn[i-2][0],cn[i-1][1]+cn[i-2][1]])
    print(cn[n][0],cn[n][1])
T=int(input())
global cn
cn=[]
cn.append([1,0])
cn.append([0,1])
cn.append([1,1])
for i in range(T):
    n=int(input())
    fibonacci(n)
    
