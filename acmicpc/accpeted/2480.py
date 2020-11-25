from collections import Counter
data = list(map(int,input().split()))
c = Counter(data).most_common()
cl = len(c)
if cl == 1: print(10000+c[0][0]*1000)
elif cl == 2:print(1000+c[0][0]*100)
else:c=sorted(c,reverse=True);print(c[0][0]*100)