arr = list(map(int,input().split()))
abc = input()
arr.sort()
dic = dict()
dic['A']=arr[0]
dic['B']=arr[1]
dic['C']=arr[2]
for i in abc:
    print(dic[i],end=' ')