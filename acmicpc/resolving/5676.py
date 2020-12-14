import sys
input = sys.stdin.readline

tree = list()
nodes = list()
def update(start,end,index,changeIdx,changeNum):
    if changeIdx <start or changeIdx>end:return 
    if start == end:
        tree[index] = changeNum
        return
    mid = (start+end)//2
    update(start,mid,index*2,changeIdx,changeNum)
    update(mid+1,end,index*2+1,changeIdx,changeNum)
    tree[index] = tree[index*2]*tree[index*2+1]
    
def query(start,end,index,left,right):
    if left>end or right<start:return 1
    if left<=start and right>=end:
        return tree[index]
    mid = (start+end)//2
    return query(start,mid,index*2,left,right)*query(mid+1,end,index*2+1,left,right)
    
def init(start,end,index):
    if start==end:
        tree[index] = nodes[start]
        return tree[index]
    mid = (start+end)//2
    tree[index] = init(start,mid,index*2)*init(mid+1,end,index*2+1)
    return tree[index]
    
if __name__ == "__main__":   
    while True:
        n,k = map(int,input().rstrip().split())
        tree = [0]*(n*4)
        nodes = list(map(int,input().rstrip().split()))
        answer = ''
        init(0,n-1,1)
        for _ in range(k):
            lst = input().rstrip().split()
            if lst[0] == 'C':#수정
                i,V = map(int,(lst[1],lst[2]))
                update(0,n-1,1,i-1,V)               
                nodes[i-1]=V      
            else:#출력
                i,j = map(int,(lst[1],lst[2]))
                if(query(0,n-1,1,i-1,j-1)==0):answer+='0'
                elif(query(0,n-1,1,i-1,j-1)>0):answer+='+'
                else:answer+='-'
        print(answer)

