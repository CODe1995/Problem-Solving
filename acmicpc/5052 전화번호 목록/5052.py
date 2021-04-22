import sys
input =sys.stdin.readline
TC = int(input())
for tc in range(1,TC+1):
    N = int(input())
    nums = [list(input().strip()) for _ in range(N)]
    nums.sort()
    answer='YES'
    for i in range(1,N):
        for j in range(len(nums[i-1])):
            if nums[i-1][j]!=nums[i][j]:
                break
        else:#일치
            answer='NO'
            break
    print(answer)