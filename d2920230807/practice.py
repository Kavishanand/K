sent="Hai I'm Niranjan and Im from Nagercoil"

word=sent.split()
c={
   'count' :0,
   'word':' '}
vowels='aeiouAEIOU'
for i in word:
    # print(i)
    wordcnt=0
    for j in i:
        if j in vowels:
            wordcnt=wordcnt+1
            
    if wordcnt>c["count"]:
        c['word']=i
        c["count"]=wordcnt
print(c)



                
              


