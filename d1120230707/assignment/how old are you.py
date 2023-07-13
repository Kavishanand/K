name=input('Hey, What is your name?') 
age=int(input(f"ok,{name},how old are you?"))

if(age>25):
    print("you can do anything that is legal.")
if(age<25):
    print("you can not rent a car.")
if(age<18):
    print("you can not vote.")
if(age<16):
    print("you can not drive.")