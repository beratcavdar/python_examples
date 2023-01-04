import time
import os
def pyramid(n):
    for i in range(1,n+1):
        if i <= n-1:
            for k in range(n-i):
                print(" ",end="")
            for l in range(2*i-1):
                if l == 0 or l == 2*i-2:
                    print("*",end="")
                else:
                    print(" ",end="")
            print()
    print("*"*(2*n-1))
while(True):
    for i in range(1,10):
        os.system("cls")
        pyramid(i)
        time.sleep(0.05)
    for i in range(10,1,-1):
        os.system("cls")
        pyramid(i)
        time.sleep(0.1)