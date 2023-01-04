n=5
for i in range(1,n+1):
    for k in range(n-i):
        print(" ",end="")
    for l in range(2*i-1):
        if l == 0 or l == 2*i-2:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    if i == 5:
        for i in range(1,n+1):
            for a in range(i-1):
                print(" ",end="")
            for b in range(2*(n-i)+1):
                if b == 0 or b == 2*(n-i):
                    print("*",end="")
                else:
                    print(" ",end="")
            print()