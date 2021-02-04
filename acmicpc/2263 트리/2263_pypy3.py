import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
N = int(input())
inorder = list(map(int,input().split()))
postorder = list(map(int,input().split()))
pos = [0]*(N+1)
for i in range(N):
    pos[inorder[i]]=i
#VLR - preorder
def solution(inStart,inEnd,postStart,postEnd):
    if inStart>=inEnd or postStart>=postEnd:return
    root = postorder[postEnd-1]
    # sys.stdout.write(str(root)+" ")#속도는 빠르지만, 메모리를 더 먹음
    print(root,end=" ")#속도는 느리지만, 메모리를 덜 먹음.
    mid=pos[root]
    leftsize = mid-inStart
    solution(inStart,mid,postStart,postStart+leftsize)#L
    solution(mid+1,inEnd,postStart+leftsize,postEnd-1)#R    
    return

if __name__=="__main__":
    solution(0,N,0,N)