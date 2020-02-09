num1 = input()
num2 = int(input())
num1L=num1[len(num1)-2:len(num1)]#뒤에 두자리만
num1 = int(num1)-int(num1L)#뒤에 두자리를 00으로 만든다
while num1%num2!=0:
    num1=num1+1
print(str(num1)[len(str(num1))-2:len(str(num1))])