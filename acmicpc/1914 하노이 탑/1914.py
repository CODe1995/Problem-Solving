import sys
N = int(input())
string = ""
dp = [0]*101
for i in range(1,101):
    dp[i]=dp[i-1]*2+1
def hanoi(_num,_from,_sub,_to):#원판갯수,출발지,목적지,임시기둥
    global string
    if _num==0:return
    hanoi(_num-1,_from,_to,_sub)
    # if N<=20:
    #     string+=str(_from)+" "+str(_to)+"\n"
    sys.stdout.write(str(_from)+" "+str(_to)+"\n")
    hanoi(_num-1,_sub,_from,_to)
if N>=21:
    print(dp[N])
else:
    print(dp[N])
    hanoi(N,1,2,3)    
# if N<=20:
#     print(string)