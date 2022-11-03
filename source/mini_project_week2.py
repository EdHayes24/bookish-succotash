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
from msilib.schema import Error, Feature
import mini_project_wk2_v1 as mp
import os
import tabulate
from datetime import datetime

def options_selector(options_list, message=None, err_msg=None):
    # Function to ask user to choose an option from the printed list
    # Args:
    # options = list or tuple, list of options to choose from
    # message = string, printed sub-menu header
    # err_msg = 
    print(message)
    print(err_msg)
    for i, option in enumerate(options_list):
        print(f"{i} = {option}")
    try:
        choice = int(input("Please Enter the ID of the desired Option: "))
        print(f"You have selected: {options_list[choice]}")
    except IndexError as ide:
        print(f"Error {ide} ")
        err_msg = "*** Please enter an integer value within {range(len())}"
        choice = options_selector(options_list, message, err_msg)
        return(choice)
    except Exception as e:
        print(f"Error {e} ")
        err_msg = "*** Please enter an integer corresponding to the desired options:"
        choice = options_selector(options_list, message, err_msg)
        return(choice)
    else:
        return(choice)


def print_list_of_dicts(list_of_dicts):
    # requires tabulate: https://pypi.org/project/tabulate/
    # Prints formatted table from list of dictonary objects using tabulate package
    # Args: list_of_dicts = list of dictionaries
    headers = list_of_dicts[0].keys()
    rows = [dict_obj.values() for dict_obj in list_of_dicts]
    print(tabulate.tabulate(rows, headers))


def order_operations_menu(products_list, orders_list):
    # Function for the order operations Options Menu
    # Prints welcome string and product operation options
    # Returns: update to stored products list, file & user input
    mutable_pl = products_list[:]
    mp.cafe_header()
    # Order Operations Constants:
    status_options = ("Preparing", "Awaiting-Delivery", "Out-for-Delivery", "Delivered")
    order_keys_usr = ("Name", "Address", "Tel", "Items")
    order_keys_sys = ("Status", "Time")
    order_keys_all = ("Name", "Address", "Tel", "Status", "Time", "Items")
    print(" Orders Dictionary Operations Menu ".center(50, '~'))
    try:
        usr_input = int(input("Option 0: exit() \nOption 1: Print Orders Dictionary \nOption 2: Create New Order \nOption 3: Update Order Status \nOption 4: Update Existing Order v2 \nOption 5: Delete Order   \n>>> Select Option No.: "))
    except Exception as e:
        print(f"Error: {e}")
        print("Please enter an integer value for the desired option")
        order_operations_menu(products_list, orders_list)
    else:
        if usr_input == 0:
            print("exiting to main menu")
            print("***** Call: main_options_menu()")
            # main_options_menu()
        elif usr_input == 1:
            # Option 1: Print Orders Dictionary
            os.system("cls")
            print_list_of_dicts(orders_list)
            order_operations_menu(products_list, orders_list)
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
            order_operations_menu(products_list, orders_list)
        elif usr_input == 3:
            # Option 3: Update Status of existing order
            # User Inputs which order they wish to amend:
            order_no = options_selector(orders_list, "Update Order Status: ")
            # User Inputs which new status they wish to assign:
            new_status = status_options[options_selector(status_options, "Choose New Order Status: ")]
            order = orders_list[order_no]
            order["Status"] = new_status
            order_operations_menu(products_list, orders_list)
        elif usr_input == 4:
            # Option 4: Amend Existing Order of User Inputs:
            # User Inputs which order they wish to amend:
            order_no = options_selector(orders_list, "Amend Existing Order: ")
            # User Inputs which data they wish to amend
            order = orders_list[order_no]
            info_change = options_selector(order_keys_usr, "Order Information Categories: ")
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
            if more_changes == "y":
                print("DEV NOTE We need to code in a recursive feature to change variables...")
            else:
                print("Returning to order operations menu")
            order_operations_menu(products_list, orders_list)
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
        else:
            print("bye!")



def products_list_operations_menu(products_list):
    # Function for the products list operation Options Menu
    # Prints welcome string and product operation options
    # Returns: update to stored products list, file & user input
    mutable_pl = products_list[:]
    cafe_header()
    print(" Products List Operations Menu ".center(50, '~'))
    try:
        usr_input = int(input("Option 0: exit() \nOption 1: Print Orders Dictionary \nOption 2: Create New Order \nOption 3: Update Order Status \nOption 4: Update Existing Order v2 \nOption 5: Delete Order   \n>>> Select Option No.: "))
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
            for i in range(len(products_list)):
                print(f"No. {i} - {products_list[i]}")
        elif usr_input == 2:
            print("create new product")
            new_product = input("insert new product name: ")
            mutable_pl = products_list_add(mutable_pl, new_product)
            products_list = commit_changes(products_list, mutable_pl)
            print_list(products_list)
        elif usr_input == 3:
            print("Update existing product")
            for i in range(len(products_list)):
                print(f"{i}={products_list[i]}")
            idx_to_update = int(input("Insert Index of product to be updated: "))
            new_product = input("insert new product name: ")
            mutable_pl[idx_to_update] = new_product
            products_list = commit_changes(products_list, mutable_pl)
        elif usr_input == 4:
            print("Delete existing product")
            for i in range(len(products_list)):
                print(f"{i}={products_list[i]}")
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

import pickle

if __name__ == "__main__":
    #mp.main_options_menu()
    products_list = mp.line_delim_txt_to_list("./data/products_list_v4.txt")
    # We need a submenu for the order operations menu
    main_menu_option = int('2')
    if main_menu_option == 2:
        # execute order operations menu
        print("entering order operations menu")
        dict1 = {"Name":"Dave Davison", "Address": "The Pub", "Tel":"01204123456", "Status":"preparing", "Time": "now", "Items":["fanta", "coke"]}
        dict2 = {"Name":"Dave Dimbleby", "Address": "The Other Pub", "Tel":"0161654321", "Status":"you've eaten it you fatty boom boom!", "Time":"later", "Items":["coke", "polos"]}
        orders_list = [dict1, dict2]
        order_operations_menu(products_list, orders_list)
        print(orders_list)
        orders_list_file = "./data/orders_list.pkl"
        with open(orders_list_file, 'wb') as handle:
            pickle.dump(orders_list, handle, protocol=pickle.HIGHEST_PROTOCOL)

