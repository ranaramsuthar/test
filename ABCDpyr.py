num=65
for i in range(50):
    for j in range(i+1):
        ch=chr(num)
        print(ch,end=" ")
        num+=1
    print('\r')
