entry=input('Are you ready for a quiz?\nokay,here it comes!')
v=0

capital=int(input('Q1) What is the capital of Alaska?\n\t1)Melbourne\n\t2)Anchorage\n\t3)Juneau\n'))
if(capital==1 or capital==2):
    print("that's wrong")
if(capital==3):
    print("that's right")


store=int(input('Q2)Can you store the value "cat"in a variable of type int?\n\t1)yes\n\t2)no\n'))
if(store==1):
    print("sorry,'cat' is a string.ints can only store numbers.")
if(store==2):
    print("that's right")


result=int(input('Q3)what is the result of 9+6/3?\n\t1)5\n\t2)11\n\t3)15/3\n'))
if(result==2):
    print("That's correct")
if(result==1):
    print("That's incorrect")

if(capital==3):
    v=v+1
if(store==2):
    v=v+1
if(result==2):
    v=v+1
    
    
print(f"Overall, you got {v} out of 3 correct.\nThanks for playing")

    
        







