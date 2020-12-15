a,b = input().split()
a = '0b'+a
b = '0b'+b
print(str(bin(int(a,2)+int(b,2)))[2:])