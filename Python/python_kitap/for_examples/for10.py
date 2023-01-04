n=5 
for i in range(1,n+1):
    for k in range(i-1):
        print(" ",end="")
    for l in range(2*(n-i)+1):
        print("*",end="")
    print()