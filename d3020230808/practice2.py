nums=[[1,2],[3,4]]
op=input('operators:')
a=0
s=[]
for i in nums:
    # print(i)
    for j in range(len(i)):
        # print(j)
        if op=='+':
            a=i[j]+a
        elif op=='str':
            s.append(i[j])

if op=='+':
    print(a)
else:
    print(s)

