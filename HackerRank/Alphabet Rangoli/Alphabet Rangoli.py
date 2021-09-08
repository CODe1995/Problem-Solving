def print_rangoli(size):
    n = 4*size-3
    alpha = 'abcdefghijklmnopqrstuvwxyz'

    for i in range(size-1, -size, -1):
        string = '-'.join(alpha[size-1:abs(i):-1] + alpha[abs(i):size])
        print(string.center(n, '-'))
    
print_rangoli(4)