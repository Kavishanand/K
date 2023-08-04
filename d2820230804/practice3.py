senten=str("Hai I'm Niranjan and Im from Nagercoil")

a=0
word=(senten.split())
# print(word)
for i in word:
    for j in range(len(i)):
    #     print(j,end=' ')
    # print(' ')
        if j>a:
            a=j
print(i)
    




