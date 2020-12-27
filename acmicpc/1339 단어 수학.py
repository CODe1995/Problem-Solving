##########################################################
import sys
input = sys.stdin.readline
def ip():return input().rstrip()
def lip():return list(input().rstrip())
def ii():return int(input())
def mii():return map(int,input().rstrip().split())
def lmii():return list(map(int,input().rstrip().split()))
##########################################################
n = ii()
alpha = [[0,i] for i in range(27)]
tree = list()
for _ in range(n):
    tmp = lip()
    lentmp = len(tmp)
    for i in range(lentmp):
        alpha[ord(tmp[i])-65][0]+=10**(lentmp-i-1)
alpha.sort(reverse=True)
ans = 0
number = 9
for num,idx in alpha:
    if num==0:break
    ans+=num*number
    number-=1
print(ans)