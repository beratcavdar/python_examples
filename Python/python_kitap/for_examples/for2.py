"Square"
# for i in range(10):
#     for i in range(10):
#         print("*", end= "")
#     print()


"Delikli kare"
# for  i in range(1):
#     for i in range(5):
#         print("*", end="")
#     print()
# for i in range(3):
#     for k in range(1):
#         print("*",end="")
#     print()
# for i in range(1):
#     for  i in range(5):
#         print("*", end="")
#     print()


"Üçgenlerr"
# for i in range(1,8):
#     for j in range(1, i+1):
#         print("*", end="")
#     print()


# for i in range(1,8):
#     for a in range(1, i+1):
#             print("*", end="")
#     print()

"Ters üçgen"
for i in range(5):
    for k in range(1,5-i):
        print(" ", end="")
    for j in range(0, i+1):
        print("*", end="")
    print()
    


for a in range(5):
    for  b in range(0, a+1 ):
        print("*", end="")
    print()

for x in range(5):
    for y in range(1, 5-x):
        print(" ",end="")
    for z in range(0, 1+x):
        print("*",end="")
    print()