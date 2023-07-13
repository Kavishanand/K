#Ye olde keychain shoppe

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
        add_keychain()

    elif menu==2:
        remove_keychain()

    elif menu==3:
        view_order()

    else:
        checkout()

menu_function()        



        
        

    





    