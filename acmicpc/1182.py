arr = [None]
changepos = 0
def main():
    global arr, changepos
    N,S = map(int,input().split())
    arr = list(map(int,input().split()))
    arr.sort()
    cnt = 0
    changepos = 0
    for i in range(1,len(arr)):
        arr[i] += arr[i-1]
        if arr[i]>arr[i-1] and changepos==0:changepos=i

    start = 1
    end = changepos    

    while start<=end and end<len(arr):
        presum = prefix(start,end)        
        if presum == S:
            cnt+=1
            start+=1
        elif presum < S:
            end+=1
        else:
            start+=1
    # print(arr,changepos)
    print(cnt)

def prefix(t,f):    #to, from
    # print(t-1,f,arr[t-1]-arr[f])
    if changepos >1:
        return -arr[f]+arr[t-1]
    else:
        return arr[f]-arr[t-1]

if __name__ == "__main__":
    main()