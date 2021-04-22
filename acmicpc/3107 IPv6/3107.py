origin_string = input()
split_string = origin_string.split(':')

#1. 빈자리 채우기
appendIndex = -1
if(len(split_string))!=8:
    index = 0
    while index<len(split_string):
        if split_string[index]=='':
            if appendIndex==-1:
                appendIndex=index
            split_string.pop(index)
            index-=1
        index+=1

size = len(split_string)
for i in range(8-size):
    split_string.insert(appendIndex,'0000')

#2. 0생략 찾기
for i in range(len(split_string)):
    if len(split_string[i]) == 4:continue
    split_string[i] = '0'*(4-len(split_string[i]))+split_string[i]


print(':'.join(split_string))

