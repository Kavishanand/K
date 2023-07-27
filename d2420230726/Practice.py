n=4

# for i in range(0,n):
#     print(end="")
#     for i in range(0,n):
#         print('*',end=" ")
#     print(" ")

for i in range (n*n,0,-1):
    if i%n==0:
         print("\n")
    print(i,end=" ")


