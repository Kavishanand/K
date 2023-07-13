name=input('Hey,what is your name?(sory,I keep forgetting.)')
age=int(input(f"ok,{name}.how old are you?"))

if(age<16):
    print(f"you can't drive.{name}")
elif(age>16 and  age<17):
    print(f"you can drive but note vote.{name}")
elif(age>18 and age<24):
    print(f"you can vote but not rent a car.{name}")
elif(age>25):
    print(f"you can do preety much anything")