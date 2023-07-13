gender=input("What is you'r gender (M or F)? ")
f_name=input('First name? ')
l_name=input('Last name? ')
age=int(input('age? '))
married=input(f"Are you married.{f_name}(y or n)?")

if(gender=='m')and(age>20):
    print(f"Then I shall call you Mr.{f_name}{l_name}.")
else:
    print(f"Then I shall call you {f_name}{l_name}.")
if(gender=='f')and(age<20):
    print(f"Then I shall call you {f_name}{l_name}.")
    if(age>=20)and(married=='y'):
        print(f"Then I shall call you Mrs.{f_name}{l_name}.")
    elif(married=='n'):
            print(f"Then I shall call you Ms.{f_name}{l_name}.")


