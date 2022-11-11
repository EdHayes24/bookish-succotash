import os
import pickle
import pyfiglet
from datetime import datetime
# Load Local Function Files:
from fileHandler_helper_functions import *
from decoration_helper_functions import *
from err_catching_helper_functions import *
from unique_str_helper_functions import *


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

def plo_new(products_list=[]):
    # Function for the products list operation Options Menu
    # Prints welcome string and product operation options
    # Returns: update to stored products list, file & user input
    # Amendment 1: load in a fake products list from csv
    products_list = read_list_of_dicts_from_csv("./data/products_list.csv")
    print(products_list)
    mutable_pl = products_list[:] # literal copy of original list 
    cafe_header()
    carryOn = True
    submenu_options = ("exit()", "Show Food Menu", "Create New Product", "Update Existing Product", "Delete a Product")
    usr_input = options_selector(submenu_options, " Products List Operations Menu ".center(50, '*'))
    if usr_input == 0:
        print("exiting to main menu")
        # Save any changes that have been made
        save_list_of_dicts_to_csv(products_list, "./data/products_list.csv")
        #list_to_line_delim_txt(products_list, "./data/products_list_v4.txt")
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
        new_product = get_min_length_string("Insert New Product Name: ")
        mutable_pl = products_list_add(mutable_pl, new_product)
        print(mutable_pl)
        products_list = commit_changes(products_list, mutable_pl)
        for i, item in enumerate(products_list):
            print(f"idx:{i}, item:{item}")
    elif usr_input == 3:
        # Option 3: Update Existing Product
        idx_to_update = options_selector(products_list, " Update Existing Product ".center(50, '~'))
        new_product = get_min_length_string("Insert New Product Name: ")
        mutable_pl[idx_to_update] = new_product
        products_list = commit_changes(products_list, mutable_pl)
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

if __name__ == "__main__":
    plo_new()