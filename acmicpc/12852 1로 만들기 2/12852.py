n = int(input())
dp =[list() for _ in range(10**6+1)]
dp[1]=[1]
dp[2]=[1,2]
dp[3]=[1,3]
dp[4]=[1,2,4]
def calc(x):
    global dp
    if len(dp[x])>0:
        return dp[x]
    arr = list()
    if x%3==0:
        res = calc(x//3)+[x]
        arr.append([len(res),res])
    if x%2==0:
        res = calc(x//2)+[x]
        arr.append([len(res),res])    
    res = calc(x-1)+[x]
    arr.append([len(res),res])    
    
    arr = sorted(arr,key=lambda x:x[0])
    dp[x] = arr[0][1]
    return dp[x]

for i in range(5,n+1):
    calc(i)
print(len(dp[n])-1)
for d in range(len(dp[n])-1,-1,-1):
    print(dp[n][d],end=' ')