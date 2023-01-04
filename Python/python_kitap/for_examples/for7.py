size = 5
for i in range(1,size+1):
    for k in range(i):
        if k == 0 or k == i-1:
            print("*",end="")
        else:
            if i != size:
                print(" ",end="")
            else:
                print("*",end="")
    print() 