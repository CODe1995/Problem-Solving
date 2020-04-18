# arr = input()
arr= list('ACAA')
# 1 0 1 1
# 0 1 0 0
# 1 0 1 1
# 1 0 1 1
num = len(arr)+1
dp = [2600]*num
dp[0]=0
field = [[0]*num for _ in range(num)]

if num-1 == 1:print(1)#문자열 길이 1개

for i in range(1,num):#우하향대각 모두 1
    field[i][i]=1

for i in range(1,num):
    for j in range(1,num):
        if arr[i-1] == arr[j-1]:
            field[i][j]=1

print(i for i in field)

for i in range(1,num):    
    for j in range(i,num):
        if field[i][j]==1:               
            dp[j]=min(dp[j],dp[i-1]+1)
print(dp[-1])