# So far 1-D lists
# We need to store more info : cusomer names, address phone number + order status
# Use a 2D data structuure = dictionary
# skip adding products to the order for now

# Goals:
# creatre a prodcut/order and add to a list
# view all products or orders
# STRETCH: update or delete a product order

# Spec:
# product = string e.g. "coke zero"
# list_of_products = list_of_strings
# order = dict e.g.:
# { cust_name: John, cust_address: }
import os

def line_delim_txt_to_list(filepath):
    # Function to unpack a line delimited text file to a list of strings
    # Args: filepath = string with path to text file accesible from os.getcwd()
    # Returns: list of strings
    try:
        with open(filepath, 'r') as f:
            out_list = []
            for line in f.readlines():
                out_list.append(line.strip('\n'))
    except FileNotFoundError as fnfe:
        print(f"Error in: line_delim_txt_to_list({filepath})")
        print(f"Error Type: {fnfe}")
        print("Returning None Object")       
    except Exception as e:
        print(f"Error in: line_delim_txt_to_list({filepath})")
        print(f"Error Type: {e}")
        print("Returning None Object")
        return(None)
    else:
        return(out_list)


def list_to_line_delim_txt(list_obj, filepath):
    # Function to save a list of strings to a line delimited text file
    # Args: 
    # list_obj = list to convert to string and save
    # filepath = string, with path to text file accesible from os.getcwd()
    try:
        with open(filepath, 'w+') as f:
            list_obj = [str(item) for item in list_obj]
            f.write('\n'.join(list_obj))
    except FileNotFoundError as fnfe:
        print(f"Error in: list_to_line_delim_txt({filepath})")
        print(f"Error: {fnfe}")
    except Exception as e:
        print(f"Error in: list_to_line_delim_txt({filepath})")
        print(f"Error: {e}")

def cafe_header():
    # Function to print presentation string
    # at top of menu calls
    print(" Welcome ".center(50, '~'))
    print(" Dave's Cafe ".center(50, '~'))


def products_list_add(products_list, item):
    # Function to add an item to update/add an item to the products list
    # Args:
    # products_list = list of strings, current products_list to be updated
    # item = string, item to be added to product list
    if item in products_list:
        print("Item {item} is already in the products_list product list")
        print("Aborting products_list_add() operation")
    else:
        products_list.append(item)
    return(products_list)


def print_list(items):
    # Function to print the indices and values of a list
    # Args:
    # items = list object to be printed
    # Returns: nothing
    for i, item in enumerate(items):
        print(f"idx:{i}, item:{item}")


def commit_changes(original, updated):
    # Function to decide whether or not to commit to changes
    # original = unedited value
    # updated = altered value
    # choice = Boolean from input , True if want to keep changes
    usr_input = input("Would you like to keep these changes? (y/n): ")
    choice = usr_input.lower()[0] == "y"
    if choice:
        return(updated)
    else:
        return(original)


def products_list_operations_menu(products_list):
    # Function for the products list operation Options Menu
    # Prints welcome string and product operation options
    # Returns: update to stored products list, file & user input
    mutable_pl = products_list[:]
    cafe_header()
    print(" Products List Operations Menu ".center(50, '~'))
    try:
        usr_input = int(input("Option 0: exit() \nOption 1: Show Food Menu \nOption 2: Create New Product \nOption 3: Update Existing Product \nOption 4: Delete a Product\n>>> Select Option No.: "))
    except Exception as e:
        print(f"Error: {e}")
        print("Please enter an integer value for the desired option")
        products_list_operations_menu(products_list)
    else:
        if usr_input == 0:
            print("exiting to main menu")
            main_options_menu()
        elif usr_input == 1:
            os.system("cls")
            cafe_header()
            print(" Food Menu ".center(50, '~'))
            for i, item in enumerate(products_list):
                print(f"No. {i} - {item}")
        elif usr_input == 2:
            print("create new product")
            new_product = input("insert new product name: ")
            mutable_pl = products_list_add(mutable_pl, new_product)
            print(mutable_pl)
            products_list = commit_changes(products_list, mutable_pl)
            print_list(products_list)
        elif usr_input == 3:
            print("Update existing product")
            for i, item in enumerate(products_list):
                print(f"{i}={item}")
            idx_to_update = int(input("Insert Index of product to be updated: "))
            new_product = input("insert new product name: ")
            mutable_pl[idx_to_update] = new_product
            products_list = commit_changes(products_list, mutable_pl)
        elif usr_input == 4:
            print("Delete existing product")
            for i, item in enumerate(products_list):
                print(f"{i}={item}")
            idx_to_del = int(input("Insert Index of product to be deleted: "))
            removed_product = mutable_pl.pop(idx_to_del)
            products_list = commit_changes(products_list, mutable_pl)
        else:
            print("user input does not compute - exiting")
        # check if you want to carry on
        input_continue = input("Would the user like to continue with Products List Operations (y/n) ?: ")
        if (input_continue.lower() == "y"):
            products_list_operations_menu(products_list)
        else:         
            # Add Input to save changes to file:
            list_to_line_delim_txt(products_list, "./data/products_list_v4.txt")
            main_options_menu()

def orders_operations_menu():
    print("order_operations_menu under development - Goodbye")
    pass

def main_options_menu():
    # Function for the Main Options Menu
    # Prints welcome string and sub-menu options
    # Returns: function call to corresponding sub-menu
    # os.system('cls')
    cafe_header()
    print(" Options Menu ".center(50, '~'))
    try:
        usr_input = int(input("Options\nOption 0: exit() \nOption 1: Open Products List operations menu  \nOption 2: Open Orders Operations menu   \n>>> Select Option No.: "))
    except Exception as e:
        print(f"Error: {e}")
        print("Please enter an integer value for the desired option")
        main_options_menu()
    else:
        if usr_input == 0:
            # Option 0: Exit Program
            os.system("cls")
            print(" Thank you for visiting ")
        elif usr_input == 1:
            # Option 1: Products List Operations Menu
            products_list = line_delim_txt_to_list("./data/products_list_v4.txt")
            products_list_operations_menu(products_list)
        elif usr_input == 2:
            # Option 2: Orders Operations Menu
            products_list = line_delim_txt_to_list("./data/products_list_v4.txt")
            orders_operations_menu()
        else:
            # Input Invalid / Out of range
            os.system("cls")
            print("Invalid Input Option, please select an integer from the Options Listed: ")
            main_options_menu()

if __name__ == "__main__":
    main_options_menu()


