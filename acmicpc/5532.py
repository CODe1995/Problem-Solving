import math
l,a,b,c,d= (int(input()) for _ in range(5))
print(l-max(math.ceil(a/c),math.ceil(b/d)))