# numbers= ( 1, 2, 3, 4, 5, 6, 7, 8, 9 )
# count_odd= 0
# count_even= 0
# for x in numbers:
#     if x % 2:

##  BAYA KALİTELİ ÖRNEK KAFA YORUYOR
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())
#     liste=[]
#     for i in range(x+1):
#         for j in range(y+1):
#             for k in range(z+1):
#                 if i + j + k !=n:
#                     liste.append([i, j, k])
#     print(liste)

# # n = int(input("Give a number from 1 to 20: "))
# # i=0
# # if n<=20 and n>=1:
# #         while i!=n:
# #             print(i*i)
# #             i=i+1

n = int(input().strip())
if n%2==0:
        print("Not Weird")
else:
        print("Weird")