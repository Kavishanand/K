n=7
a=[100,180,260,310,40,535,695]
prof=0


for i in range(len(a)):
    # print(i)
    for j in range(len(a)):
        b=a[i]-a[j]

        if b > prof:
            prof=b
            c=i
            d=j
            
print("profit",prof,(c,d))

