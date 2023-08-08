lst=[2,5,8,1,9,3,7]
a=0
for i in lst:
    for j in lst:
        if i-j>a:
            a=i-j
print(a)
