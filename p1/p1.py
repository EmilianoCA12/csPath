# This project is the second one in the course of computer science
# In which we're going to be using operations to calculate the ticket 
# Of the customers of our store

# I would like to add that I'm trying to improve more
# From the expected result given the knowledge at
# This point of the course

# Products description and price
product_descriptions = ["Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.\n", 
                        "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.\n",
                        "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.\n"]

product_prices = [254.00, 180.50, 52.15]

# Tax value
sales_tax = 0.088

# Frist customer ticket initialization
customer_one_total = 0

customer_one_itemization = []

# Menu for client navegation
while True : 

    # Menu display
    print("\n-------Welcom to Lovely Loveseats-------")
    print("1.- Buy from the catalog")
    print("2.- Review ticket")
    print("3.- Finish buying")

    # User selection
    opt = int(input("Your selection: "))

    # Menu options based on decition
    # 1.- Item selection
    if opt == 1:

        # Menu customization
        print("\n-------Select your item-------")

        # Option display
        for i, item in enumerate(product_descriptions):
            print(f"{i + 1}.- {item}")
            print(f"\tPrice: {product_prices[i]}")
            print("------------------------------\n")

        # User item selection 
        selection = int(input("Desired item: ")) - 1

        # Validation of existing item
        if selection < 0 or selection > 2 :
            print("Please select an existing item\n")
        else :
            print("Good choise\n")

            # Add up to the customers ticket
            customer_one_total += product_prices[selection]
            customer_one_itemization.append(selection)
    
    # Ticket review
    elif opt == 2:
        
        # Ticket display
        print("\n-------Your ticket-------")

        for item in customer_one_itemization:
            print(f"{item + 1}.- {product_descriptions[item]}")
            print(f"Price: {product_prices[item]}")
            print("-------------------------\n")

        # Total before and after taxes
        print(f"Checkout total: ${customer_one_total}")
        print(f"Taxes deduction: ${customer_one_total * sales_tax : 10.2f}")
        print(f"Total with taxes: ${customer_one_total * (1 + sales_tax) : 10.2f}\n")

    # Checkout 
    elif opt == 3:

        # Total display
        print("\n-------Thanks for buying-------")

        # Total before and after taxes
        print(f"Checkout total: ${customer_one_total}")
        print(f"Taxes deduction: ${customer_one_total * sales_tax : 10.2f}")
        print(f"Total with taxes: ${customer_one_total * (1 + sales_tax) : 10.2f}\n")

        break

    else : 
        print("Please select a valid option\n")