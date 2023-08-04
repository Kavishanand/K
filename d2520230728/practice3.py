a=[]
A=""
B=""
C=""
while True:
    if(len(a)==10):
        break
    c=input("Enter candidate:")
    
    if (c=="A" or c=="B" or c=="C"):
        a.append(f"Candidate:{c}")
        if (c=="A"):
            A=A+1
        if (c=="B"):
            B=B+1
        if (c=="C"):
            C=C+1
    elif(c!="A" or c!="B" or c!="C"):
        print("give correct candidate")
    
print(a)
