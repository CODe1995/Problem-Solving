import sys
from collections import deque
input = sys.stdin.readline
scoreTable = [0,0,0,1,1,2,3,5,11]#글자수별 점수
direction = [[1,0],[0,1],[-1,0],[0,-1],[-1,1],[1,1],[-1,-1],[1,-1]]
w = int(input().rstrip())   #사전 단어의 개수
dictionary = list()
arr = list()

class Node(object):#TRIE
    def __init__(self,key,data=None):
        self.head  = Node(None)
        self.key = key 
        self.data = data 
        self.children = {}
    
    '''
    트라이에 문자열 삽입
    '''
    def insert(self, string):
        curr_node = self.head
        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)

            curr_node = curr_node.children[char]
            # string의 마지막 글자 차례이면,
            # 노드의 data 필드에 저장하려는 문자열 전체를 저장한다.(옵션)
        curr_node.data = string
    
    '''
    주어진 단어 string이 트라이에 존재하는지 여부를 반환
    '''
    def search(self, string):
        curr_node = self.head

        for char in string:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False
        #string의 마지막 글자에 도달했을 때,
        #curr_node에 data가 있다면 string이 트라이에 존재하는 것
        if curr_node.data!=None:
            return True

    def starts_with(self,prefix):
        curr_node = self.head
        result = []
        subtrie = None

        #트라이에서 prefix를 찾고,
        #prefix의 마지막 글자 노드를 subtrie로 설정
        for char in prefix:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
                subtrie = curr_node
            else:
                return None
        
        #bfs로 prefix subtrie를 순회하며
        #data가 있는 노드를(=완전한 단어) 찾는다.
        dq = deque(subtrie.children.values())
        while dq:
            curr=dq.pop()
            if curr.data != None:
                result.append(curr.data)
            dq += deque(curr.children.values())
        return result

for _ in range(w):
    dictionary.append(input().rstrip())

input()
b = int(input().rstrip())   #보드의 개수

for i in range(b):
    arr = [['' for _ in range(4)] for _ in range(4)]
    for j in range(4):
        arr[i][j] = input().rstrip().split()
    #얻을 수 있는 최대 점수, 가장 긴 단어, 찾은 단어의 수
    arr.sort()

    if i+1!=b:
        input()
for ar in arr:
    print(ar)

