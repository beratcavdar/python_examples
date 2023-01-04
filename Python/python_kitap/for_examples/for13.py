n=5
for i in range(1,n+1):
    if i == 5:
        
        continue

    for l in range(i-1):
        print(" ",end="")

    for k in range(2*(n-i)+1):
        print("*",end="")

    print()
if i == 5:
    for i in range(1,n+1):
        for k in range(n-i):
            print(" ",end="")
        for l in range(0,2*i-1):
            print("*",end="")
        print()