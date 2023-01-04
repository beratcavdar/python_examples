n=5
for i in range(1,n+1):
    for k in range(n-i):
        print(" ",end="")
    for l in range((2*i)-1):
        print("*",end="")
    print()
if i == 5:
    for a in range(1,n+1):
        for b in range(a-1):
            print(" ",end="")
        for c in range(2*(n-a)+1):
            print("*",end="")
        print()
