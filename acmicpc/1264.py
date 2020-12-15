di = 'AaEeIiOoUu'
while True:
    a = input() 
    cnt=0   
    if a=='#':
        break
    else:
        for word in a:
            if word in di:
                cnt+=1
        print(cnt)    