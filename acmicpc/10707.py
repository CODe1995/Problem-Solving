a,b,c,d,P = (int(input()) for _ in range(5))
xfee = a*P
yfee = b
if P>c:yfee+=(P-c)*d
print(min(xfee,yfee))