
# Initiate variables
choice = 0
invalid_counter = 0
total = 0
owner_firstName = "Douglass"
owner_lastName = "Coronado"
invalid_choice = "error: Invalid choice"
multiple_invalid_options = "error: Your time has expired!!"
your_option = "your option:  "

def menu():
    print("\n\n")
    print("| 1. Peperoni Pizza          ...     $14.00  |")
    print("| 2. Chicken Mushroom Pizza  ...     $15.00  |")
    print("| 3. Beef Mexican Pizza      ...     $13.00  |")
    print("| 4. Vegetable Pizza         ...     $10.00  |")
    print("| 5. Cheese Pizza            ...     $9.00   |")
    print("| 6. Quit                                    |\n\n")

def welcome_message(firstName,lastName):
    print("\n\nGreetings from "+firstName+"-"+lastName+" Pizza Heaven!!!!!\n\n")

def get_pizza_price(order_number):

    if order_number == 1:
        pizza_price = 14.00
    elif order_number == 2:
        pizza_price = 15.00
    elif order_number == 3:
        pizza_price = 13.00
    elif order_number == 4:
        pizza_price = 10.00
    elif order_number == 5:
        pizza_price = 9.00
    elif order_number == 6:
        print("Quit")
        pizza_price = 0.00
    else:
        print("\n"+invalid_choice.upper())
        pizza_price = 0.00
    
    return pizza_price

def get_pizza_name(order_number):
    if order_number == 1:
        pizza = "Peperoni Pizza"
    elif order_number == 2:
        pizza = "Chicken Mushroom Pizza" 
    elif order_number == 3:
        pizza = "Beef Mexican Pizza"
    elif order_number == 4:
        price = "Vegetable Pizza"
    elif order_number == 5:
        pizza = "Cheese Pizza" 
    else:
        pizza = "No choice made"
    
    return pizza

def get_method_payment(payment):

    if payment == 1:
        method = "Credit"
    elif payment == 2:
        method = "Debit"
    else:
        method = "Cash"

    return method
    
def menu_size():

    print("\n\n")
    print("| 1. Regular         ...     $0.00  |")
    print("| 2. Large           ...     $2.00  |")
    print("| 3. Extra Large     ...     $4.00  |")

def get_size_price(size):
    if size == 1:
        size_price = 0
    elif size == 2:
        size_price = 2.00
    elif size == 3:
        size_price = 4.00
    else:
        size_price = -1 
        print("\n"+invalid_choice.upper())

    return size_price

def method_payment(payment):

    if payment == 1:
        method = "Credit"
    elif payment == 2:
        method = "Debit"
    else:
        method = "Cash"

    return method

def payment_options():

    print("\n\n")
    print("| 1. Credit  |")
    print("| 2. Debit   |")
    print("| 3. Cash    |")


welcome_message(owner_firstName,owner_lastName)

# Input from customer
client_firstName = raw_input("What is your first name?  ")
client_lastName =  raw_input("What is your last name?   ")

# Output message
print("\nHi, I am "+owner_firstName+", what do you want to order today with us?\n")
print("We have the following menu:\n\n")


while choice != 6:
    
    # display menu and select choice
    menu()
    choice = int(input(client_firstName+" "+client_lastName+" ,let me know what is your choice?  "))

    # if the customer choose a pizza
    if choice >= 1 and choice <= 5:
        # get the pizza price
        price = get_pizza_price(choice)
        total += float(price)
        # get the selected pizza name 
        pizza_name = get_pizza_name(choice)

        # display this message once - choosing pizza size
        print("\n\nThank you for choosing "+pizza_name)
        print("All the size is regular, if you want to order large you have to add $2. If you want extra large then you have to add $4")
        print("Please choose from the following options:\n\n")
        size_price = -1

        while size_price < 0:
            print ("YOUR PIZZA:  "+pizza_name)
            menu_size()
            size = int(input("\n\n"+your_option.upper()))
            size_price = get_size_price(size)

        total += size_price
        response = "no"

        while (choice != 6) and (choice != -1):
            response = str(raw_input("\n\nDo you want to order more pizza? then type 'YES' to add more order or 'NO' to finalize the order:  "))
            if response == "no" or response == "NO":
                print("\n\nYour complete order price is: $"+str(total)+"\nHow would you like to pay? ")
                payment_options()
                print ("\n\n")
                option = int(input("\n\n"+your_option.upper()))
                print ("\nYour payment method is:  "+get_method_payment(option))
                print("\nThank you for ordering with "+client_firstName+" "+client_lastName+" Pizza Heaven, we would love to see you again")
                choice = 6
            elif response == "yes" or response == "YES":
                choice = -1
            else:
                choice = 0
                invalid_counter += 1
                if invalid_counter == 3:
                    print(multiple_invalid_options.capitalize())
                    choice = 6
    elif choice == 6:
        print ("If you din't find what you wanted, please leave your comments")
        comments = raw_input("Please let us know your feedback:  ")
        if comments:
            print ("\n\nYour feedback: \t\t"+comments+"\n\nThanks for your feedback, your comments will be sent to our customer service manager")
        print("\n\nThank "+client_firstName+" for chosing "+owner_firstName+" "+owner_lastName+" Pizza Heaven")
    else:
        invalid_counter += 1
        print(invalid_choice.upper())
        if invalid_counter == 3:
            print(multiple_invalid_options.capitalize())
            choice = 6





