lst=[3,2,2,3,2]
a=[]
for i in range(len(lst)):
    if (lst[i]!=3):
        a=a+[lst[i]]
# print(a)
for j in range(0,len(lst)):
    if (lst[j]!=2):
        a=a+["*"]
print(a)


    
        

