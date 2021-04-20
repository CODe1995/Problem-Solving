order = list(input())
arr = []
for i in range(len(order)):
    arr.append([order[i],i])#value,index
visited = [0]*len(order)
def makeStr(x):
    string = ''
    for i in range(len(x)):
        string+=x[i][0]
    return string
def deepCopy(a,b):#a를 b로 복사(from,to)
    for i in range(len(a)):
        b.append(a[i])
    return b
def dfs(depth,temp):
    if depth==len(arr):
        return
    minValue = makeStr(temp)    
    saveTemp = list()
    minIndex = -1
    for i in range(len(arr)):
        if visited[i]:continue
        newTemp = list()
        newTemp = deepCopy(temp,newTemp)
        newTemp.append([arr[i][0],arr[i][1]])
        newTemp = sorted(newTemp,key=lambda x:x[1])
        newstr = makeStr(newTemp)
        if minValue == makeStr(temp):#init 비교군이 없을때
            minValue = newstr
            minIndex = i
            saveTemp = newTemp
        elif minValue>newstr:
            minValue = newstr
            minIndex = i
            saveTemp = newTemp
    print(minValue)    
    visited[minIndex]=True
    dfs(depth+1,saveTemp)
dfs(0,list())
        
        