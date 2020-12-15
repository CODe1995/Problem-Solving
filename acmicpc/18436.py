import sys
input = sys.stdin.readline

tree_even= list()   #짝수 트리
tree_odd = list()   #홀수 트리
nodes = list()

def update(start,end,index,cidx,diff):
    if cidx < start or end < cidx: return       
    if start==end:
        if diff%2==0 and nodes[cidx]%2==0:#기존 짝수 -> 짝수
            pass
        elif diff%2==0 and nodes[cidx]%2!=0:#홀-짝
            tree_even[index]+=1
            tree_odd[index]-=1
        elif diff%2!=0 and nodes[cidx]%2==0:#짝-홀
            tree_odd[index]+=1
            tree_even[index]-=1
        else:#홀>홀
            pass
        return
    mid = (start+end)//2
    update(start,mid,index*2,cidx,diff)
    update(mid+1,end,index*2+1,cidx,diff)
    tree_even[index] = tree_even[index*2]+tree_even[index*2+1]
    tree_odd[index] = tree_odd[index*2]+tree_odd[index*2+1]

def query_even(start,end,index,left,right):
    if left>end or right<start:
        return 0
    if left <=start and end <= right:
        return tree_even[index]
    mid = (start+end)//2
    return  query_even(start,mid,index*2,left,right)+query_even(mid+1,end,index*2+1,left,right)
def query_odd(start,end,index,left,right):
    if left>end or right<start:
        return 0
    if left <=start and end <= right:
        return tree_odd[index]
    mid = (start+end)//2
    return  query_odd(start,mid,index*2,left,right)+query_odd(mid+1,end,index*2+1,left,right)

def init_even(start,end,index):#짝수
    if start==end:
        if nodes[start]%2==0:
            tree_even[index] += 1
        return tree_even[index]
    mid = (start+end)//2
    tree_even[index] = init_even(start,mid,index*2)+init_even(mid+1,end,index*2+1)
    return tree_even[index]
def init_odd(start,end,index):#홀수
    if start==end:
        if nodes[start]%2!=0:
            tree_odd[index] += 1
        return tree_odd[index]
    mid = (start+end)//2
    tree_odd[index] = init_odd(start,mid,index*2)+init_odd(mid+1,end,index*2+1)
    return tree_odd[index]

if __name__ == "__main__":
    n = int(input())
    tree_even = [0]*(n*4)
    tree_odd = [0]*(n*4)
    nodes = list(map(int,input().rstrip().split()))
    m = int(input())
    init_even(0,n-1,1)
    init_odd(0,n-1,1)
    for _ in range(m):
        a,b,c = map(int,input().rstrip().split())
        if a==1:# b를 c로 바꾼다.
            update(0,n-1,1,b-1,c)        
            nodes[b-1]=c    
        elif a==2:# 짝수 개수를 출력한다.
            if b>c:b,c=c,b
            print(query_even(0,n-1,1,b-1,c-1))              
        else:# 홀수 개수를 출력한다. 
            if b>c:b,c=c,b
            print(query_odd(0,n-1,1,b-1,c-1))