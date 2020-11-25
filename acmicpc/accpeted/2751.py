import sys

inpt = sys.stdin.readline
arr= []
for i in range(int(inpt().rstrip())):
    arr.append(int(inpt().rstrip()))
arr = sorted(arr)
for i in arr:
    print(i)

# #하나가 될 때까지 쪼개는 함수
# def splitup(data):
#     if len(data) <= 1:  # data 갯수가 하나라면 굳이 쪼갤 필요가 없음!
#         return data
#     mid = len(data)//2  # //는 나머지를 버린다!
#     leftList = splitup(data[:mid])  # 가운데까지가 왼쪽 -> 계속 쪼개기
#     rightList = splitup(data[mid:])  # 가운데부터는 오른쪽 -> 계속 쪼개기
#     return sort(leftList, rightList)  # 최종적으로 정렬된 데이터를 반환해라!


# #쪼개진걸 정렬하는 함수
# def sort(left, right):
#     result = []
#     while len(left) > 0 or len(right) > 0:
#         if len(left) > 0 and len(right) > 0:
#             if left[0] <= right[0]:
#                 result.append(left[0])
#                 left = left[1:]
#             elif left[0] >= right[0]:
#                 result.append(right[0])
#                 right = right[1:]
#         elif len(left) > 0:
#             result.append(left[0])
#             left = left[1:]
#         elif len(right) > 0:
#             result.append(right[0])
#             right = right[1:]
#     return result


# N = int(sys.stdin.readline())
# data = []
# for i in range(N):
#     data.append(int(sys.stdin.readline()))
# data = splitup(data)
# for i in range(N):
#     sys.stdout.write(str(data[i])+'\n')