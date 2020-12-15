n = int(input())

cnt = 0
num = 666
while cnt!=n:
    if str(num).find('666')>-1:
        cnt+=1
    num+=1 
print(num-1)
