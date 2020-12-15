from collections import Counter
n= int(input())
for i in range(n):
    army = list(map(int,input().split()))
    tmp = Counter(army[1:]).most_common()     
    if len(tmp)==1:
        print(tmp[0][0])
    else: 
        if tmp[0][1]>tmp[1][1] and len(army[1:])/2<tmp[0][1]:
            print(tmp[0][0])
        else:
            print('SYJKGW')
