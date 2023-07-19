#Keychains for sale,for real this time.
print('Ye old Keychain shoppe')

current=0
price=10

def add_keychain(current):
    add=int(input(f"you have {current} key chains, how many add :"))
    current=current+add
    print(f"now you have {current}keychains")
    return current
    
def remove_keychain(current):
    remove=int(input(f"you have {current} key chains, how many remove :"))
    current= current-remove
    print(f"now you have {current}keychains")
    return current
    
def view_order(current,price):
    
    print(f"you have {current} keychains")
    print(f"keychain cost ${price} each")
    price=current*price
    print(f"total cost is ${price}")
    return price
          
def checkout(current,price):
    print("check out")
    name=str(input("what is your name? "))
    print(f"you have {current}keychains.")
    print(f"keychain cost $10 each.\nTotal cost is ${price}")
    print(f"Thanks for you order{name}!")


while True:

    menu=int(input('1. Add Keychain to order\n2. Remove Keychain from Order \n3. View Current Order\n4. Check out\nPlease enter your choice  '))
    
    if menu==1:
        current=add_keychain(current)
    
    elif menu==2:
        current=remove_keychain(current)

    elif menu==3:
        price=view_order(current,price)

    elif menu==4:
        checkout(current,price)
        break
    




    
