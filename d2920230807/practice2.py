senten=("the quick brown fox jumps over the lazy dog the quick brown fox")

word=senten.split()
c={}
for i in word:
        if i in c:
            c[i]=c[i]+1
        else:
            c[i]=1

print(c)