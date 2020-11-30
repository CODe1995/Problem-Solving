s = int(input())
n=0
for i in range(1,s+1):    
    n+=i
    if n>s:
        print(i-1)
        break