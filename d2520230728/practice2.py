#method 1

a="kavish"
b=""

for i in a:
    b=i+b
print(b)
    
#method 2

a="level"
b="level"

for i in range(len(a),-1,-1):
    b=a[i]+b
    print(b)
