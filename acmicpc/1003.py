def fibonacci(n):
    if cn[n]!=[0,0]:
        return cn[n]
    
    return cn[n]
T=int(input())
global cn
cn=[[0,0]*42]
cn[0]=[1,0]
cn[1]=[0,1]
cn[2]=[1,1]
for i in range(T):
    n=int(input())
    print(fibonacci(n))
    
