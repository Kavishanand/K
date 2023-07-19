print('I will add up the number you give me')

num=int(input('number: '))

while True:

    total=int(input(f"The total so far is {num}\n number: "))
    
    num=num+total

    if total==0:
        break
    print(f"The total is {num}.")

    


