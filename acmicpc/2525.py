h,m = map(int,input().split())
t = int(input())
m=m+t
if m>59:
    l=m//60
    h+=l
    m=m%60
if h>23:    
    h%=24
print(h,m)