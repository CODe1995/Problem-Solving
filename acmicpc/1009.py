import sys
input = sys.stdin.readline
dictionary = {
    0:[10],
    1:[1],
    2:[2,4,8,6],
    3:[3,9,7,1],
    4:[4,6],
    5:[5],
    6:[6],
    7:[7,9,3,1],
    8:[8,4,2,6],
    9:[9,1]
}
T = int(input().rstrip())
for _ in range(T):
    a,b = map(int,input().rstrip().split())
    print(dictionary[int(str(a)[-1])][b%len(dictionary[int(str(a)[-1])])-1])

'''
0 10
1 1
2 2 4 8 6
3 3 9 7 1
4 4 6
5 5
6 6
7 7 9 3 1
8 8 4 2 6
9 9 1
'''