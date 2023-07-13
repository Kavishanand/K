name=input("Enter your name:  ")
age =int(input("Enter your age:  "))
dob =input("Enter yor DOB:  ")
location  =input("Enter location:  ")
college =input("Enter college name:  ")
print('hello,my name is',name,'i am ',age,'year old and was born on',dob,'currently,i am located in',location,'and i completed my degree at',college,)


age=int(input('Enter your age: '))
print(age)
if (age >= 18):
    print('your eligible to vote')
else :
    print ('your not eligible')


number=int(input('Enter the number; '))
print(number)
if (number%2==0):
    print (number, 'is an even number')
else :
    print (number, 'is an odd number')  


item1=int(input("Enter the amount of item1: "))
item2=int(input("Enter the amount of item2: "))
item3=int(input("Enter the amount of item3: "))
item4=int(input("Enter the amount of item4: "))
items=item1+item2+item3+item4
 
if (items < 1000) and (items > 500):
    print('you have owned a silver token')
if (items < 500):
    print ('you have owned a 0 token') 
if (items > 1000):  
    print ('you have owned a golden token')