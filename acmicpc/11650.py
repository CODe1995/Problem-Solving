import sys
input = sys.stdin.readline

lst = list()
for _ in range(int(input().rstrip())):
    lst.append(list(map(int,input().rstrip().split())))
for i in list(sorted(lst,key=lambda x: [x[0],x[1]])):
    print(i[0],i[1])
