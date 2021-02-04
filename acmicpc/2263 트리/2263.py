import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
N = int(input())
inorder = list(map(int,input().strip().split()))
postorder = list(map(int,input().strip().split()))
#VLR - preorder
def solution(inStart,inEnd,postStart,postEnd):
    if len(inorder[inStart:inEnd])==0:return
    root = postorder[postEnd-1]
    sys.stdout.write(str(root)+" ")#V
    if len(inorder[inStart:inEnd])==1:return
    mid=0
    for i in range(inStart,inEnd):
        if inorder[i]==root:
            mid = i
            break
    leftsize = len(inorder[inStart:mid])
    rightsize = len(inorder[mid+1:inEnd])
    solution(inStart,mid,postStart,postStart+leftsize)#L
    solution(mid+1,inEnd,postStart+leftsize,postEnd-1)#R    
    return

if __name__=="__main__":
    solution(0,N,0,N)