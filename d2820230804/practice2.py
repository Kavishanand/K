num=int(input("Enter a num:"))


# for i in range(num+1):
#     print('*'*i)
# for j in range(num-1,0,-1): 
#     print('*'*j) 
    

for i in range(1,num*2):
    if i<=num:
        a=i
    else:
        a=(num*2)-i
    for k in range(a):
        print('*',end=' ')
    print(' ')


    