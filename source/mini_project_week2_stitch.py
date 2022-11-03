#import mini_project_wk2_v1 as mp
import os
import tabulate
import pickle
import pyfiglet
from datetime import datetime

# import pyfiglet module
import pyfiglet


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


def cafe_header():
    # Function to print presentation string
    # at top of menu calls
    os.system("cls")
    print(pyfiglet.figlet_format("Dave's Cafe", font = "fuzzy" ))
    print(" Welcome ".center(50, '~'))
    print(" Dave's Cafe ".center(50, '~'))


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


def print_list_of_dicts(list_of_dicts):
    # requires tabulate: https://pypi.org/project/tabulate/
    # Prints formatted table from list of dictonary objects using tabulate package
    # Args: list_of_dicts = list of dictionaries
    headers = list_of_dicts[0].keys()
    rows = [dict_obj.values() for dict_obj in list_of_dicts]
    print(tabulate.tabulate(rows, headers))


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


def order_operations_menu(products_list, orders_list):
    # Function for the order operations Options Menu
    # Prints welcome string and product operation options
    # Returns: update to stored products list, file & user input
    cafe_header()
    # Order Operations Constants:
    status_options = ("Preparing", "Awaiting-Delivery", "Out-for-Delivery", "Delivered")
    order_keys_usr = ("Name", "Address", "Tel", "Items")
    order_keys_sys = ("Status", "Time")
    order_keys_all = ("Name", "Address", "Tel", "Status", "Time", "Items")
    submenu_options = ("exit()", "Print Orders Dictionary", "Create New Order", "Update Order Status", "Update Existing Order", "Delete Order")
    carryOn = True
    # Retrieve User Input to navigate submenu
    usr_input = options_selector(submenu_options, " Orders Dictionary Operations Menu ".center(50, '*'))
    if usr_input == 0:
        print("exiting to main menu")
        # Save any changes that have been made
        orders_list_file = "./data/orders_list.pkl"
        with open(orders_list_file, 'wb') as handle:
            pickle.dump(orders_list, handle, protocol=pickle.HIGHEST_PROTOCOL)
            carryOn = False # Set recursion in submenu to false
        # main_options_menu()
    elif usr_input == 1:
        # Option 1: Print Orders Dictionary
        os.system("cls")
        print_list_of_dicts(orders_list)
    elif usr_input == 2:
        # Option 2: Create a New Order
        print("Create New Order:")
        # Initialise Order Dict and recieve User info
        dict_obj = {}
        for key in order_keys_usr:
            if key == "Items":
                dict_obj[key] = products_list
            else:
                dict_obj[key] = input(f"Please Insert Order {key}: ")
        order_time = str(datetime.today().strftime('%Y-%m-%d'))
        # Add System Input Information to Order Dict
        dict_obj["Time"] = order_time
        dict_obj["Status"] = status_options[0]
        order_uniq_id = "_".join([order_time, str(1+len(orders_list)).zfill(3)]) + "_" + "_".join(dict_obj["Name"].split())
        print(order_uniq_id)
        # Add dictionary object to orders_dict dictionary
        orders_list.append(dict_obj)
    elif usr_input == 3:
        # Option 3: Update Status of existing order
        # User Inputs which order they wish to amend:
        order_no = options_selector(orders_list, "Update Order Status: ".center(50, " "))
        # User Inputs which new status they wish to assign:
        new_status = status_options[options_selector(status_options, "Choose New Order Status: ".center(50, " "))]
        order = orders_list[order_no]
        order["Status"] = new_status
    elif usr_input == 4:
        # Option 4: Amend Existing Order of User Inputs:
        # User Inputs which order they wish to amend:
        order_no = options_selector(orders_list, "Amend Existing Order: ".center(50, " "))
        # User Inputs which data they wish to amend
        more_changes = "y"
        while more_changes == "y":
            order = orders_list[order_no]
            info_change = options_selector(order_keys_usr, "Order Information Categories: ".center(50, " "))
            info_change_key = order_keys_usr[info_change]
            if info_change_key == "Items":
                print("DEV NOTE: WE NEED ADDITIOANL Feature to deal with this")
            # Request User Input for new value
            print(f"Current value of {info_change_key} is: {order[info_change_key]}")
            new_variable = input(f"Please insert new value for {info_change_key}: ")
            usr_confirm = input("Is this correct? (y/n): ")
            if usr_confirm.lower() == "y":
                order[info_change_key] = new_variable
            else:
                print(f"Changes to {info_change_key} Cancelled")
            more_changes = input("Is there anything else to amend on this order? (y/n): ")
        print("\nReturning to order operations menu\n")
    elif usr_input == 5:
        # Option 5: Delete an Order
        # User Inputs which order they wish to amend:
        order_no = options_selector(orders_list, "Delete An Order: ")
        order = orders_list[order_no]
        print("Order to be Deleted: ")
        print_list_of_dicts(orders_list[order_no])
        usr_confirm = input("Is this correct?")
        if usr_confirm == "y":
            orders_list.remove(orders_list[order_no])
    # Recursion if carryOn is True, present submenu options again
    # Else exit back to previous menu
    if carryOn == True:
        input("\n Press Any Key To Continue: \n    > ")
        order_operations_menu(products_list, orders_list)
    else:
        main_options_menu()


def products_list_operations_menu(products_list):
    # Function for the products list operation Options Menu
    # Prints welcome string and product operation options
    # Returns: update to stored products list, file & user input
    mutable_pl = products_list[:] # literal copy of original list 
    cafe_header()
    carryOn = True
    submenu_options = ("exit()", "Show Food Menu", "Create New Product", "Update Existing Product", "Delete a Product")
    usr_input = options_selector(submenu_options, " Products List Operations Menu ".center(50, '*'))
    if usr_input == 0:
        print("exiting to main menu")
        # Save any changes that have been made
        list_to_line_delim_txt(products_list, "./data/products_list_v4.txt")
        carryOn = False # Set recursion in submenu to false
    elif usr_input == 1:
        # Option 1: Print Products List
        os.system("cls")
        cafe_header()
        print(" Food Menu ".center(50, '~'))
        for i, item in enumerate(products_list):
            print(f"No. {i} - {item}")
    elif usr_input == 2:
        # Option 2: Create a New Product
        print(" Create a New Product ".center(50, '~'))
        new_product = input("insert new product name: ")
        mutable_pl = products_list_add(mutable_pl, new_product)
        print(mutable_pl)
        products_list = commit_changes(products_list, mutable_pl)
        for i, item in enumerate(products_list):
            print(f"idx:{i}, item:{item}")
    elif usr_input == 3:
        # Option 3: Update Existing Product
        idx_to_update = options_selector(products_list, " Update Existing Product ".center(50, '~'))
        new_product = input("insert new product name: ")
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
        products_list_operations_menu(products_list)
    else:
        main_options_menu()


def main_options_menu():
    # Function for the Main Options Menu
    # Prints welcome string and sub-menu options
    # Returns: function call to corresponding sub-menu
    # os.system('cls')
    cafe_header()
    menu_options = ("exit()","Open Products List operations menu", "Open Orders Operations menu")
    usr_input = options_selector(menu_options, " Options Menu ".center(50, '~'))
    print(" Options Menu ".center(50, '~'))
    if usr_input == 0:
        # Option 0: Exit Program
        os.system("cls")
        print(pyfiglet.figlet_format("Goodbye", font = "fuzzy" ))
        print(" Thank you for visiting ")
    elif usr_input == 1:
        # Option 1: Products List Operations Menu
        products_list = line_delim_txt_to_list("./data/products_list_v4.txt")
        products_list_operations_menu(products_list)
    elif usr_input == 2:
        # Option 2: Orders Operations Menu
        orders_list_file = "./data/orders_list.pkl"
        with open(orders_list_file, 'rb') as handle:
            orders_list = pickle.load(handle)
        products_list = line_delim_txt_to_list("./data/products_list_v4.txt")
        order_operations_menu(products_list, orders_list)
    else:
        # Input Invalid / Out of range
        os.system("cls")
        print("Invalid Input Option, please select an integer from the Options Listed: ")
        main_options_menu()


if __name__ == "__main__":
    main_options_menu()
    orders_list_file = "./data/orders_list.pkl"
    with open(orders_list_file, 'rb') as handle:
        orders_list = pickle.load(handle)
    for order in orders_list:
        print(order)