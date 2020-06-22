arr = list(map(int,input().split()))
abc = input()
arr.sort()
dic = dict()
dic['a']=arr[0]
dic['b']=arr[1]
dic['c']=arr[2]
for i in abc:
    print(dic[i],end=' ')