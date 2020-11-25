t = int(input())
for i in range(1,t):
    il = list(map(int,list(str(i))))
    if i+sum(il)==t:
        print(i)
        t=0
        break
if t!=0 :print(0)
