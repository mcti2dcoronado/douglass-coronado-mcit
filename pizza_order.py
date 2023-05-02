pizza_name = ""
total = 0
dict_menu = {"1":"Peperoni Pizza","2":"Chicken Mushroom Pizza","3":"Beef Mexican Pizza","4":"Vegetable Pizza","5":"Cheese Pizza","6":"No Pizza"}
dict_size={"1":"Regular","2":"Large","3":"Extra Large"}
dict_payment_method = {"1":"Credit", "2":"Debit","3":"Cash"}
response = "yes"


def menu_display(dict_menu):
    print (dict_menu)

def welcome_message(firstName,lastName):
    print("Greetings from "+firstName+"-"+lastName+" Pizza Heaven!!!!!\n\n")
    print("I am "+firstName+", what do you want to order today with us?\n")
    print("We have the following menu:\n")

def choose_menu(order_number):

    if order_number == 1:
        price = 14
    elif order_number == 2:
        price = 15
    elif order_number == 3:
        price = 13
    elif order_number == 4:
        price = 10
    elif order_number == 5:
        price = 9 
    else:
        price = 0
    
    return price

def name_pizza(order_number):
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
        pizza = "No pizza"
    
    return pizza


    
def display_extra_menu(pizza_name):
    print("Thank you for choosing "+pizza_name+", all the size is regular, if you want to order large you have to add $2. If you want extra large then you have to add $4")
    print("Please choose from the following options:")

def method_payment(payment):

    if payment == 1:
        method = "Credit"
    elif payment == 2:
        method = "Debit"
    else:
        method = "Cash"

    return method

def pizza_size_price(size):

    if size == 1:
        size_price = 0
    elif size == 2:
        size_price = 2
    else:
        size_price = 4

    return size_price



firstName = input("What is your first name? ")
lastName = input("What is your last name? ")

welcome_message(firstName,lastName)



while response == "yes":
   
    menu_display(dict_menu)
    order_number = int(input("Please type the number in front of each pizza to add them to the order:"))
    price_pizza = choose_menu(order_number)

    if price_pizza > 0:
        total += price_pizza
        print(total)
        pizza_name = name_pizza(order_number)
        display_extra_menu(pizza_name)
        print(dict_size)
        size = int(input("What is your pizza selected size?"))
        price_size = pizza_size_price(size)
        total += price_size

        response = input("Do you want to order more pizza? then type 'yes' to add more to the order or 'no' to finalize the order")
        if response == "yes":
            print(dict_menu)
        else:
            print("Your complete order price is: $"+str(total))
            print("How whould you like to pay?")
            print(dict_payment_method)

        payment = int(input("What is your method payment?"))
        print("Your payment method is: ",method_payment(payment))
        response = "no"
    else:
       response = "no"


print("Thank you for ordering with "+firstName+"-"+lastName+"Pizza Heaven, we would love to see you again")
