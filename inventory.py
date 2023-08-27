#========The beginning of the class==========
class Shoe:

    # Initiate the attributes of the class
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
    
    # Method to return the cost of the shoes
    def get_cost(self):
        print(f"The cost of the shoes is: R{self.cost}")


    # Method to return the quantity of the shoes
    def get_quantity(self):
        print(f"The quantity of the shoes is: {self.quantity}")

    # Method to return a string representation of a class
    def __str__(self):
        return f"Country: {self.country} \nCode: {self.code} \nProduct: {self.product} \nCost: {self.cost} \nQuantity: {self.quantity}"


#=============Shoe list===========

# Create an empty list to store a list of objects of shoes.
shoe_list = []


#==========Functions outside the class==============

def read_shoes_data():
    # Make use of try-except for error handling
    try:
        with open("inventory.txt", "r") as file:
            # Skip the first line in the file
            next(file)

            for line in file:
                temp = line.strip().split(",")

                # Create a shoes object with the data and appen this into the shoes list
                if len(temp) == 5:
                    country, code, product, cost, quantity = temp
                    shoe = Shoe(country, code, product, float(cost), int(quantity))
                    shoe_list.append(shoe)
                else:
                    print(f"Invalid data format: {line}")

    # Inform the user for the instance of the File not found
    except FileNotFoundError:
        print(f"File not found.")

    except Exception as e:
        print(f"An error occured: {e}")

    # Return the appended shoe list
    return shoe_list

   
def capture_shoes():
    # Obtain data from the user to append to the shoe list
    new_country = input("Please provide the country of the product: ")
    new_code = input("Please provide the product code: ")
    new_product = input("Please provide the product name: ")
    new_cost = float(input("Please provide the cost of the product: "))
    new_quantity = int(input("Please provide the quantity of the product: "))

    # Append new object into the shoe list
    new_item = Shoe(new_country, new_code, new_product, new_cost, new_quantity)
    shoe_list.append(new_item)
    

def view_all():
    print("\nAll Shoes:")
    print(f"{'Country':<15} {'Code':<10} {'Product':<25} {'Cost':<10} {'Quantity':<10}")

    # Iterate through each item in the shoe list and print the details, aligning all elements
    for shoe in shoe_list:
        # Format costs to two decimal places
        cost_formatted = f"${shoe.cost:.2f}"
        print(f"{shoe.country:<15} {shoe.code:<10} {shoe.product:<25} {cost_formatted:<10} {shoe.quantity:<10}")
    

def re_stock(shoe_list, file_name):
    # Find the item with the lowest quantity and ask the user with how much they want to restock it with
    # Use 'min' to find the shoe with the lowest quantity
    min_quantity_shoe = min(shoe_list, key=lambda shoe: shoe.quantity)
    
    print("Shoe with the lowest quantity:")
    print(min_quantity_shoe)
    
    # Use try-except to avoid the instance were the user enters an invalid quantity integer
    try:
        restock_quantity = int(input(f"How many {min_quantity_shoe.product} shoes do you want to restock? "))

        # Add the desired number to the quantity of the shoe with the current lowest quantity
        min_quantity_shoe.quantity += restock_quantity

        # Update the quantity in the file
        with open(file_name, 'r') as file:
            lines = file.readlines()

        with open(file_name, 'w') as file:
            for line in lines:
                temp = line.strip().split(',')
                if len(temp) == 5 and temp[1] == min_quantity_shoe.code:
                    temp[4] = str(min_quantity_shoe.quantity)
                    updated_line = ','.join(temp)
                    file.write(updated_line + '\n')
                else:
                    file.write(line)

        print(f"{restock_quantity} {min_quantity_shoe.product} shoes have been restocked.")

     # Inform the user if an invalid quantity has been entered
    except ValueError:
        print("Invalid input. Please enter a valid quantity.")


def search_shoe(shoe_list, shoe_code):
    # Loop through items in shoes_list, return shoe if shoe_code is found
    for shoe in shoe_list:
        if shoe.code == shoe_code:
            return shoe
    
    # If shoe_code is not found in shoes_list, return none
    return None


def value_per_item(shoe_list):
    # Calculate the total value for each item in the shoe list, and print all values
    print("\nValue per item for all shoes:")
    for shoe in shoe_list:
        value = shoe.cost * shoe.quantity
        print(f"{shoe.product}: ${value:.2f}")
    

def highest_qty(shoe_list):
    # Find the item with the maximum quantity
    max_quantity_shoe = max(shoe_list, key=lambda shoe: shoe.quantity)

    print(f"The shoe with the highest quantity is for sale:")
    print(max_quantity_shoe)
    

#==========Main Menu=============

while True:
    # Print the Main Menu items
    print("\n====== Shoe Inventory Management ======")
    print("1. Read Shoes Data")
    print("2. Capture Shoes")
    print("3. View All Shoes")
    print("4. Re-stock")
    print("5. Search Shoe")
    print("6. Value per Item")
    print("7. Highest Quantity")
    print("8. Exit")
    
    # Obtain the user's choice
    choice = input("Select an option from the above Menu: ")

    # Check the user's choice and perform the corresponding action
    if choice == "1":
        # Read shoe data from file
        shoe_list = read_shoes_data()
        print("\nThe \"Inventory\" file has been scanned and a list has been created containing all shoes in inventory.")

    elif choice == "2":
        # Capture new shoe data
        capture_shoes()

    elif choice == "3":
        # View details of all shoes
        view_all()

    elif choice == "4":
        # Restock shoes
        re_stock(shoe_list, "inventory.txt")

    elif choice == "5":
        # Search for a specific shoe by shoe code
        shoe_code = input("\nEnter the shoe code to search: ")
        found_shoe = search_shoe(shoe_list, shoe_code)
        if found_shoe:
            print("\nShoe found:")
            print(found_shoe)
        else:
            print("\nShoe not found.")

    elif choice == "6":
        # Calculate and print value per item for all shoes
        value_per_item(shoe_list)

    elif choice == "7":
        # Find and print shoe with the highest quantity
        highest_qty(shoe_list)

    elif choice == "8":
        # Exit the program
        print("\nExiting the program.")
        break

    else:
        # Invalid choice
        print("\nInvalid choice. Please select a valid option.")