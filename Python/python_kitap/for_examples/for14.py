n=5
for i in range(n+1):
    for k in range(i):
        print("*",end="")
    print("")
for i in range(n):
    for l in range(n-i-1):
        print("*",end="")
    print()