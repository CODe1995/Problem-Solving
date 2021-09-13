import sys,os

N = int(input())
arr = list()
maxindex = 0
highest = 0 #최고 높이
mid = 0
for i in range(N):
    a = list(map(int,input().split()))    
    arr.append(a)
    #가장 높은 막대의 index가 mid
    if highest<a[1]:
        highest=a[1]
        mid=a[0]
    maxindex = max(maxindex,a[0])
arr.sort()

warehouse = [0]*(maxindex+1)
for i in range(len(arr)):
    warehouse[arr[i][0]] = arr[i][1]

s,e = arr[0][0],mid
weight = 0
prev = -1
while s<e and s<=maxindex:    
    if warehouse[s]>prev or prev==-1:#높이 갱신
        prev = warehouse[s]
    weight += prev
    s+=1

s,e = arr[-1][0],mid
prev = -1
while s>e and s>=arr[0][0]:
    if warehouse[s]>prev or prev==-1:
        prev = warehouse[s]
    weight += prev
    s-=1
print(weight+highest)