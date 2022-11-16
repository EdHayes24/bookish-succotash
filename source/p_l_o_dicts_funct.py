import os
import pickle
import pyfiglet
from datetime import datetime
# Load Local Function Files:
from fileHandler_helper_functions import *
from decoration_helper_functions import *
from err_catching_helper_functions import *
from unique_str_helper_functions import *

# DEV NOTES:
# Need to remove return() statment at bottom of function!


# # # User Input Helper Functions:
def options_selector(options_list, message="\n", err_msg="\n"):
    # Function to ask user to choose an option from the printed list
    # Args:
    # options = list or tuple, list of options to choose from
    # message = string, printed sub-menu header
    # err_msg = string, informs user of correct input format based on prior error
    print(message)
    print(err_msg)
    for i, option in enumerate(options_list):
        print(f"{i} = {option}")
    try:
        choice = int(input("Please Enter the ID of the desired Option: "))
        print(f"You have selected: {options_list[choice]}")
    except IndexError as ide:
        print(f"Error {ide} ")
        err_msg = f"*** Please enter an integer value within {range(len(options_list))}"
        choice = options_selector(options_list, message, err_msg)
        return(choice)
    except Exception as e:
        print(f"Error {e} ")
        err_msg = "*** Please enter an integer corresponding to the desired options:"
        choice = options_selector(options_list, message, err_msg)
        return(choice)
    else:
        return(choice)

# # # List operations Helper Functions:
def products_list_add(products_list, item):
    # Function to add an item to update/add an item to the products list
    # Args:
    # products_list = list of strings, current products_list to be updated
    # item = string, item to be added to product list
    if item in products_list:
        print(f"Item {item} is already in the products_list product list")
        print("Aborting products_list_add() operation")
    else:
        products_list.append(item)
    return(products_list)

def append_to_list_of_dicts(list_of_dicts):
    # Function to add a new Dict Entry to a list of dictionaries
    # Args: 
    # 
    list_of_dicts = list_of_dicts
    pass

courier_1 = {"Name": "Tim", "Tel": 123456789, "Orders": [1,2,3]}
courier_2 = {"Name": "Simon", "Tel": 987654321, "Orders": [4,5,6]}
list_of_couriers = [courier_1, courier_2]
save_list_of_dicts_to_csv(list_of_couriers, "./data/couriers_list.csv")


products_list = read_list_of_dicts_from_csv("./data/products_list.csv")
couriers_list = read_list_of_dicts_from_csv("./data/couriers_list.csv")



def plo_new(products_list=[]):
    # Function for the products list operation Options Menu
    # Prints welcome string and product operation options
    # Returns: update to stored products list, file & user input
    product_keys = ("Name", "Price")
    product_dtype = ("str", "float")
    #products_list = read_list_of_dicts_from_csv("./data/products_list.csv")
    print(products_list)
    mutable_pl = products_list[:] # literal shallow copy of original list 
    cafe_header()
    carryOn = True
    submenu_options = ("exit()", "Show Food Menu", "Create New Product", "Update Existing Product", "Delete a Product")
    usr_input = options_selector(submenu_options, " Products List Operations Menu ".center(50, '*'))
    if usr_input == 0:
        print("exiting to main menu")
        # Save any changes that have been made
        save_list_of_dicts_to_csv(products_list, "./data/products_list.csv")
        carryOn = False # Set recursion in submenu to false
    elif usr_input == 1:
        # Option 1: Print Products List
        os.system('cls||clear')
        cafe_header()
        print(" Food Menu ".center(50, '~'))
        print_list_of_dicts(products_list)
    elif usr_input == 2:
        # Option 2: Create a New Product
        print(" Create a New Product ".center(50, '~'))
        new_product_name = get_min_length_string("Insert New Product Name: ")
        all_product_names = [d.get("Name") for d in products_list]
        if (new_product_name in all_product_names):
            # Product already exists in List of Dictionaries
            print(f"{new_product_name} already exists in Products List")
            print("Aborting Add operation...\n")
        else:
            # Product has no existing key, continue
            new_product_price = round(get_non_neg_float("Insert New Product Price: ", 2))
            new_product = {"Name":new_product_name, "Price":new_product_price}
            mutable_pl.append(new_product)
            products_list = commit_changes(products_list, mutable_pl)
            print_list_of_dicts(products_list)
    elif usr_input == 3:
        # Option 3: Update Existing Product
        product_no = options_selector(products_list, " Update Existing Product ".center(50, '~'))
        info_change = options_selector(product_keys, "Product Information Categories: ".center(50, " "))
        info_change_key = product_keys[info_change]
        if info_change_key == "Name":
            new_var = get_min_length_string("Insert New Product Name: ")
        elif info_change_key == "Price":
            new_var = get_non_neg_float("Insert New Product Price: ")
        # Make Shallow Copy of Dictionary to decide if you want to keep your changes
        mutable_dict = mutable_pl[product_no].copy()
        # Update Copy and check if user wants to keep changes
        mutable_dict[info_change_key] = new_var
        products_list[product_no] = commit_changes(products_list[product_no], mutable_dict)
    elif usr_input == 4:
        # Option 4: Delete an Existing Product
        idx_to_del = options_selector(products_list, " Delete Existing Product ".center(50, '~'))
        removed_product = mutable_pl.pop(idx_to_del)
        products_list = commit_changes(products_list, mutable_pl)
    # Recursion if carryOn is True, present submenu options again
    # Else exit back to previous menu
    if carryOn == True:
        input("\n Press Any Key To Continue: \n    > ")
        plo_new(products_list)
    else:
        return()
        main_options_menu()


def clo_new(couriers_list):
    # Function for the courier operations Options Menu
    # Prints welcome string and product operation options
    # Returns: update to stored products list, file & user input
    courier_keys = ("Name", "Tel", "Orders")
    courier_dtype = ("str", "str", "lst")
    mutable_co = couriers_list[:]
    cafe_header()
    # courier Operations Constants:
    submenu_options = ("exit()", "Print Couriers List", "Add New Courier", "Update Existing Courier", "Delete Courier")
    carryOn = True
    # Retrieve User Input to navigate submenu
    usr_input = options_selector(submenu_options, " Courier Operations Menu ".center(50, '*'))
    if usr_input == 0:
        print("exiting to main menu")
        # Save any changes that have been made
        #list_to_line_delim_txt(couriers_list, "./data/couriers_list.txt")
        save_list_of_dicts_to_csv(couriers_list, "./data/couriers_list.csv")
        carryOn = False # Set recursion in submenu to false
    elif usr_input == 1:
        # Option 1: Print Couriers List
        os.system('cls||clear')
        print(" Couriers ".center(50, '~'))
        print_list_of_dicts(couriers_list)
    elif usr_input == 2:
        # Option 2: Add a New Courier
        print(" Add a New Courier ".center(50, '~'))
        new_courier_name = get_min_length_string("Insert New Courier Name: ")
        all_courier_names = [d.get("Name") for d in couriers_list]        # Make Sure Courier name is unique
        if new_courier_name in all_courier_names:
            print("Courier already exists in list\nGenerating Unique Name for courier")
            print(f"New Courier Name: {new_courier_name}")
            new_courier_name = make_string_unique(new_courier_name, all_courier_names)
        new_courier_tel = get_min_length_string("Insert Courier Tel: ")
        new_courier_orders = []
        new_courier = {"Name": new_courier_name, "Tel":new_courier_tel, "Orders": new_courier_orders}
        mutable_co.append(new_courier)
        print(mutable_co)
        couriers_list = commit_changes(couriers_list, mutable_co)
        print_list_of_dicts(couriers_list)
    elif usr_input == 3:
        # Option 3: Update Existing Courier
        # User Inputs which Courier they wish to amend:
        courier_no = options_selector(couriers_list, " Update Existing Courier ".center(50, '~'))
        more_changes = "y"
        while more_changes == "y":
            info_change = options_selector(courier_keys, "Courier Information Categories: ".center(50, " "))
            info_change_key = courier_keys[info_change]
            if info_change_key == "Orders":
                # Make a Function to add an Order to the List
                print("DEV NOTE: Need to add orders to Courier objects using a function")
                print("This also needs to update said orders")
                print("OOP am I right?")
            elif info_change_key == "Name":
                # Ensure Courier Name is Unique
                new_var = get_min_length_string(f"Insert New Courier {info_change_key} :")
                all_courier_names = [d.get("Name") for d in couriers_list]        # Make Sure Courier name is unique
                if new_var in all_courier_names:
                    print("Courier already exists in list\nGenerating Unique Name for courier")
                    print(f"New Courier Name: {new_var}")
                    new_var = make_string_unique(new_var, all_courier_names)   
            else:
                new_var = get_min_length_string(f"Insert New Courier {info_change_key} :")
            usr_confirm = get_min_length_string("Is this correct? (y/n): ")
            if usr_confirm.lower() == "y":
                    couriers_list[courier_no][info_change_key] = new_var
            else:
                print(f"Changes to {info_change_key} Cancelled")
            more_changes = input("Is there anything else to amend on this order? (y/n): ")
        print("\nReturning to order operations menu\n")
    elif usr_input == 4:
        # Option 4: Delete a Courier
        courier_no = options_selector(couriers_list, " Delete Existing Courier ".center(50, '~'))
        courier = couriers_list[courier_no]
        print("Courier to be Deleted: ")
        print_list_of_dicts([couriers_list[courier_no]])
        usr_confirm = input("Is this correct? (y/n): ")
        if usr_confirm.lower() == "y":
            couriers_list.remove(couriers_list[courier_no])
    # Recursion if carryOn is True, present submenu options again
    # Else exit back to previous menu  
    if carryOn == True:
        input("\n Press Any Key To Continue: \n    > ")
        clo_new(couriers_list)
    else:
        return()
        #main_options_menu()




if __name__ == "__main__":
    plo_new(products_list)
    #clo_new(couriers_list)
