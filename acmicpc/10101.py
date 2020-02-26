from collections import Counter
data = list(int(input())for _ in range(3))
c = Counter(data).most_common()
lc = len(c)
if lc==1:print('Equilateral')
elif lc == 2 and sum(data)==180:print('Isosceles')
elif lc==3 and sum(data)==180:print('Scalene')
else:print('Error')
