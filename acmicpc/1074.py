n,r,c = map(int,input().split())
cnt = 0
size = 2**n
x,y = c,r
while True:
    if size==1:
        break
    if size/2<=x and size/2>y:#1사분면
        cnt+=(size/2)**2
        x-=size/2
    elif size/2>x and size/2>y:#2사분면
        cnt+=0
    elif size/2>x and size/2<=y:#3사분면
        cnt+=((size/2)**2) * 2
        y-=size/2
    elif size/2<=x and size/2<=y:#4사분면
        cnt+=((size/2)**2) * 3
        x-=size/2
        y-=size/2
    size/=2

print(int(cnt))