#Keychains for sale,for real this time.

print('Ye old Keychain shoppe')
 

def add_keychain():
    print('ADD KEYCHAIN')
    menu_function()
def remove_keychain():
    print('REMOVE KEYCHAIN')
    menu_function()
def view_order():
    print('VIEW ORDER')
    menu_function()
def checkout():
    print('CHECKOUT')

def menu_function():
    menu=int(input('1. Add Keychain to order\n2. Remove Keychain from Order \n3. View Current Order\n4. Check out\nPlease enter your choice  '))


    if menu==1:
        add=0
        add=input(f"You have {add} keychains.How manyto add? ")
        print(f"you now have{add+add}keychains.")
        add_keychain()
    
    elif menu==2:
        sub=0
        sub=input(f"you have {add}keychains.How many to remove? ")
        print(f"Tou have {add-sub}keychains.")
        remove_keychain()

    elif menu==3:
        cost=10
        order=input(f"You have {add-sub}Keychains.\nKeychain cost ${cost}each\nTotal cost is ${cost*add-sub}.")
        view_order()

    else:
        checkout()
        name=input(f"What is your name?")
        key=input(f"You have {add-sub}keychains.\nKeychain cost ${cost}each.\nTotal cost is ${cost*add-sub}.\nThanks for your order.{name}")




    
