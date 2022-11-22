#!/usr/bin/env python
""" 
    Bookish-Succotash - mini_project_week2_stitch.py
    A Cafe Order Menu System for managing products, couriers and orders in a CLI interface using Python.
    Main File to Run
"""
__author__ = "Edward Hayes"
__email__ = "edwardhayes@sky.com"
__status__ = "Development"

import os
import pickle
import pyfiglet
import ast
from datetime import datetime

# Load Local Function Files:
from fileHandler_helper_functions import *
from decoration_helper_functions import *
from err_catching_helper_functions import (
    get_min_length_string,
    get_non_neg_float,
    get_non_negative_int,
    options_selector,
)
from product_operations_helper_functions import *
from unique_str_helper_functions import *



def courier_operations_menu(couriers_list):
    '''Prints Welcome String for Courier List Operations\n
    Gets user input for operation to be performed and executes\n
    Saves changes to products_list, orders_list, couriers_list on exit'''
    # Function for the courier operations Options Menu
    # Prints welcome string and product operation options
    # Returns: update to stored products list, file & user input
    courier_keys = ("Name", "Tel", "Orders")
    courier_dtype = ("str", "str", "lst")
    mutable_co = couriers_list[:]
    cafe_header()
    # courier Operations Constants:
    submenu_options = (
        "exit()",
        "Print Couriers List",
        "Add New Courier",
        "Update Existing Courier",
        "Delete Courier",
    )
    carryOn = True
    # Retrieve User Input to navigate submenu
    usr_input = options_selector(
        submenu_options, " Courier Operations Menu ".center(50, "*")
    )
    if usr_input == 0:
        print("exiting to main menu")
        # Save any changes that have been made
        save_list_of_dicts_to_csv(couriers_list, "./data/couriers_list.csv")
        carryOn = False  # Set recursion in submenu to false
    elif usr_input == 1:
        # Option 1: Print Couriers List
        os.system("cls||clear")
        print(" Couriers ".center(50, "~"))
        print_list_of_dicts(couriers_list)
    elif usr_input == 2:
        # Option 2: Add a New Courier
        print(" Add a New Courier ".center(50, "~"))
        new_courier_name = get_min_length_string("Insert New Courier Name: ")
        all_courier_names = [
            d.get("Name") for d in couriers_list
        ]  # Make Sure Courier name is unique
        if new_courier_name in all_courier_names:
            print("Courier already exists in list\nGenerating Unique Name for courier")
            new_courier_name = make_string_unique(new_courier_name, all_courier_names)
            print(f"New Courier Name: {new_courier_name}")
        new_courier_tel = get_min_length_string("Insert Courier Tel: ")
        new_courier_orders = []
        new_courier = {"Name": new_courier_name, "Tel": new_courier_tel, "Orders": []}
        mutable_co.append(new_courier)
        print(mutable_co)
        couriers_list = commit_changes(couriers_list, mutable_co)
        print_list_of_dicts(couriers_list)
    elif usr_input == 3:
        # Option 3: Update Existing Courier
        # User Inputs which Courier they wish to amend:
        courier_no = options_selector(
            couriers_list, " Update Existing Courier ".center(50, "~")
        )
        more_changes = "y"
        while more_changes == "y":
            info_change = options_selector(
                courier_keys, "Courier Information Categories: ".center(50, " ")
            )
            info_change_key = courier_keys[info_change]
            if info_change_key == "Orders":
                # Make a Function to add an Order to the List
                print(
                    "DEV NOTE: Need to add orders to Courier objects using a function"
                )
                print("This also needs to update said orders")
                print("OOP am I right?")
            elif info_change_key == "Name":
                # Ensure Courier Name is Unique
                new_var = get_min_length_string(
                    f"Insert New Courier {info_change_key} :"
                )
                all_courier_names = [
                    d.get("Name") for d in couriers_list
                ]  # Make Sure Courier name is unique
                if new_var in all_courier_names:
                    print(
                        "Courier already exists in list\nGenerating Unique Name for courier"
                    )
                    new_var = make_string_unique(new_var, all_courier_names)
                    print(f"New Courier Name: {new_var}")
            else:
                new_var = get_min_length_string(
                    f"Insert New Courier {info_change_key} :"
                )
            usr_confirm = get_min_length_string("Is this correct? (y/n): ")
            if usr_confirm.lower() == "y":
                couriers_list[courier_no][info_change_key] = new_var
            else:
                print(f"Changes to {info_change_key} Cancelled")
            more_changes = input(
                "Is there anything else to amend on this Courier? (y/n): "
            )
        print("\nReturning to Courier Operations menu\n")
    elif usr_input == 4:
        # Option 4: Delete a Courier
        courier_no = options_selector(
            couriers_list, " Delete Existing Courier ".center(50, "~")
        )
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
        courier_operations_menu(couriers_list)
    else:
        main_options_menu()


def order_operations_menu(products_list, orders_list, couriers_list):
    '''Prints Welcome String for Order Operations\n
    Gets user input for operation to be performed and executes\n
    Saves changes to products_list, orders_list, couriers_list on exit'''
    # Function for the order operations Options Menu
    # Prints welcome string and product operation options
    # Returns: update to stored products list, file & user input
    cafe_header()
    # Order Operations Constants:
    status_options = ("Preparing", "Awaiting-Delivery", "Out-for-Delivery", "Delivered")
    order_keys_usr = ("Name", "Address", "Tel", "Items")
    order_keys_sys = ("Order_ID", "Status", "Time", "Courier")
    order_keys_all = (
        "Order_ID",
        "Name",
        "Address",
        "Tel",
        "Status",
        "Time",
        "Items",
        "Courier",
    )
    courier_keys = ("Name", "Tel", "Orders")
    submenu_options = (
        "exit()",
        "Print Orders Dictionary",
        "Create New Order",
        "Update Order Status",
        "Update Existing Order",
        "Delete Order",
    )
    carryOn = True
    # Retrieve User Input to navigate submenu
    usr_input = options_selector(
        submenu_options, " Orders Dictionary Operations Menu ".center(50, "*")
    )
    if usr_input == 0:
        print("exiting to main menu")
        # Save any changes that have been made
        orders_list_file = "./data/orders_list.pkl"
        with open(orders_list_file, "wb") as handle:
            pickle.dump(orders_list, handle, protocol=pickle.HIGHEST_PROTOCOL)
            carryOn = False  # Set recursion in submenu to false
        save_list_of_dicts_to_csv(couriers_list, "./data/couriers_list.csv")
        # main_options_menu()
    elif usr_input == 1:
        # Option 1: Print Orders Dictionary
        os.system("cls||clear")
        print_list_of_dicts(orders_list)
        # Add option to Sort Dictionaries
        usr_sort = get_min_length_string(
            "\n Would you like to sort the Orders List? (y/n): "
        )
        if usr_sort.lower() == "y":
            order_by = options_selector(
                order_keys_all, " Select Parameter to Sort by: ".center(50, " ")
            )
            key_to_sort_by = order_keys_all[order_by]
            if key_to_sort_by in ("Courier", "Items"):
                list_of_subkeys = list(orders_list[0][key_to_sort_by].keys())
                subkey = list_of_subkeys[
                    options_selector(
                        list_of_subkeys,
                        " Select Parameter to Sort by: ".center(50, " "),
                    )
                ]
                if subkey in ("Items"):
                    print_list_of_dicts(
                        sorted(
                            orders_list,
                            key=lambda x: x[key_to_sort_by][subkey][0]["Name"],
                        )
                    )
                else:
                    print_list_of_dicts(
                        sorted(orders_list, key=lambda x: x[key_to_sort_by][subkey])
                    )
            else:
                print_list_of_dicts(
                    sorted(orders_list, key=lambda x: x[key_to_sort_by])
                )
    elif usr_input == 2:
        # Option 2: Create a New Order
        print("Create New Order:")
        # Initialise Order Dict and recieve User info
        dict_obj = {}
        customer_selection = {"Items": [], "Quantity": []}
        for key in order_keys_usr:
            if key == "Items":
                customer_selection = product_selector(
                    1, products_list, customer_selection, ("Items", "Quantity")
                )
                dict_obj[key] = customer_selection
            else:
                dict_obj[key] = get_min_length_string(f"Please Insert Order {key}: ")
        order_time = str(datetime.today().strftime("%Y-%m-%d"))
        # Add System Input Information to Order Dict
        dict_obj["Time"] = order_time
        dict_obj["Status"] = status_options[0]
        order_uniq_id = (
            "_".join([order_time, str(1 + len(orders_list)).zfill(3)])
            + "_"
            + "_".join(dict_obj["Name"].split())
        )
        print(order_uniq_id)
        dict_obj["Order_ID"] = order_uniq_id
        courier_pick = options_selector(
            couriers_list, f"Select a Courier for the order: {order_uniq_id}"
        )
        # Upon Picking Courier, add Order_ID to the relevant Courier Dictionary
        courier = couriers_list[courier_pick]
        courier.get("Orders").append(order_uniq_id)
        dict_obj["Courier"] = courier
        # Add dictionary object to orders_dict dictionary
        orders_list.append(dict_obj)
    elif usr_input == 3:
        # Option 3: Update Status of existing order
        # User Inputs which order they wish to amend:
        order_no = options_selector(
            orders_list, "Update Order Status: ".center(50, " ")
        )
        # User Inputs which new status they wish to assign:
        new_status = status_options[
            options_selector(
                status_options, "Choose New Order Status: ".center(50, " ")
            )
        ]
        order = orders_list[order_no]
        order["Status"] = new_status
    elif usr_input == 4:
        # Option 4: Amend Existing Order of User Inputs:
        # User Inputs which order they wish to amend:
        order_no = options_selector(
            orders_list, "Amend Existing Order: ".center(50, " ")
        )
        # User Inputs which data they wish to amend
        more_changes = "y"
        while more_changes == "y":
            order = orders_list[order_no]
            info_change = options_selector(
                order_keys_usr, "Order Information Categories: ".center(50, " ")
            )
            info_change_key = order_keys_usr[info_change]
            if info_change_key == "Items":
                # Functions to add, remove, edit for customer_selection
                items_op = options_selector(
                    ("Cancel", "Add", "Remove", "Amend"),
                    "Select Items Order Amendment operation: ",
                )
                # Opens product selection menu to add, remove, edit based on user inputs
                order["Items"] = product_selector(
                    items_op, products_list, order["Items"], ("Items", "Quantity")
                )
            else:
                # Request User Input for new value
                print(
                    f"Current value of {info_change_key} is: {order[info_change_key]}"
                )
                new_variable = get_min_length_string(
                    f"Please insert new value for {info_change_key}: "
                )
                # Ask User if happy to keep proposed changes
                usr_confirm = input("Is this correct? (y/n): ")
                if usr_confirm.lower() == "y":
                    order[info_change_key] = new_variable
                else:
                    print(f"Changes to {info_change_key} Cancelled")
            more_changes = input(
                "Is there anything else to amend on this order? (y/n): "
            )
        print("\nReturning to order operations menu\n")
    elif usr_input == 5:
        # Option 5: Delete an Order
        # User Inputs which order they wish to amend:
        order_no = options_selector(orders_list, "Delete An Order: ")
        order = orders_list[order_no]
        order_id = order["Order_ID"]
        courier_name = order["Courier"]["Name"]
        # Find corresponding courier in the couriers_list
        courier_obj = next(item for item in couriers_list if item["Name"] == courier_name)
        print("Order to be Deleted: ")
        print_list_of_dicts([orders_list[order_no]])
        usr_confirm = input("Is this correct? (y/n): ")
        if usr_confirm.lower() == "y":
            courier_obj["Orders"].remove(order_id)
            orders_list.remove(orders_list[order_no])
    # Recursion if carryOn is True, present submenu options again
    # Else exit back to previous menu
    if carryOn == True:
        input("\n Press Any Key To Continue: \n    > ")
        order_operations_menu(products_list, orders_list, couriers_list)
    else:
        main_options_menu()


def products_list_operations_menu(products_list):
    '''Prints Welcome String for Products List Operations\n
    Gets user input for operation to be performed and executes\n
    Saves changes to products_list, orders_list, couriers_list on exit'''
    # Function for the products list operation Options Menu
    # Prints welcome string and product operation options
    # Returns: update to stored products list, file & user input
    product_keys = ("Name", "Price")
    product_dtype = ("str", "float")
    mutable_pl = products_list[:]  # literal copy of original list
    cafe_header()
    carryOn = True
    submenu_options = (
        "exit()",
        "Show Food Menu",
        "Create New Product",
        "Update Existing Product",
        "Delete a Product",
    )
    usr_input = options_selector(
        submenu_options, " Products List Operations Menu ".center(50, "*")
    )
    if usr_input == 0:
        print("exiting to main menu")
        # Save any changes that have been made
        save_list_of_dicts_to_csv(products_list, "./data/products_list.csv")
        carryOn = False  # Set recursion in submenu to false
    elif usr_input == 1:
        # Option 1: Print Products List
        os.system("cls||clear")
        cafe_header()
        print(" Food Menu ".center(50, "~"))
        print_list_of_dicts(products_list)
    elif usr_input == 2:
        # Option 2: Create a New Product
        print(" Create a New Product ".center(50, "~"))
        new_product_name = get_min_length_string("Insert New Product Name: ")
        all_product_names = [d.get("Name") for d in products_list]
        if new_product_name in all_product_names:
            # Product Already Exists in List of Dictionaries
            print(f"{new_product_name} already exists in Products List")
            print("Aborting Add operation...\n")
        else:
            # Product has no existing key, continue
            new_product_price = round(
                get_non_neg_float("Insert New Product Price: "), 2
            )
            new_product = {"Name": new_product_name, "Price": new_product_price}
            mutable_pl.append(new_product)
            products_list = commit_changes(products_list, mutable_pl)
            print_list_of_dicts(products_list)
    elif usr_input == 3:
        # Option 3: Update Existing Product
        product_no = options_selector(
            products_list, " Update Existing Product ".center(50, "~")
        )
        info_change = options_selector(
            product_keys, "Product Information Categories: ".center(50, " ")
        )
        info_change_key = product_keys[info_change]
        if info_change_key == "Name":
            new_var = get_min_length_string("Insert New Product Name: ")
        elif info_change_key == "Price":
            new_var = round(get_non_neg_float("Insert New Product Price: "), 2)
        # Make Shallow Copy of Dictionary to decide if you want to keep your changes
        mutable_dict = mutable_pl[product_no].copy()
        # Update Copy and check if user wants to keep changes
        mutable_dict[info_change_key] = new_var
        products_list[product_no] = commit_changes(
            products_list[product_no], mutable_dict
        )
    elif usr_input == 4:
        # Option 4: Delete an Existing Product
        idx_to_del = options_selector(
            products_list, " Delete Existing Product ".center(50, "~")
        )
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
    # os.system('cls||clear')
    cafe_header()
    menu_options = (
        "exit()",
        "Open Products List operations menu",
        "Open Orders Operations menu",
        "Open Courier Operations Menu",
    )
    usr_input = options_selector(menu_options, " Options Menu ".center(50, "~"))
    print(" Options Menu ".center(50, "~"))
    if usr_input == 0:
        # Option 0: Exit Program
        os.system("cls||clear")
        print(pyfiglet.figlet_format("Goodbye", font="fuzzy"))
        print(" Thank you for visiting ")
    elif usr_input == 1:
        # Option 1: Products List Operations Menu
        products_list = read_list_of_dicts_from_csv("./data/products_list.csv")
        products_list_operations_menu(products_list)
    elif usr_input == 2:
        # Option 2: Orders Operations Menu
        orders_list_file = "./data/orders_list.pkl"
        with open(orders_list_file, "rb") as handle:
            orders_list = pickle.load(handle)
        products_list = read_list_of_dicts_from_csv("./data/products_list.csv")
        couriers_list = read_list_of_dicts_from_csv("./data/couriers_list.csv")
        # Due to a list being stored in the value of key: Orders inside couriers_list
        # We need to execute an operation to convert each value upon read to enable list operations
        # Will this break them? Maybe we convert when run?
        for d in couriers_list:
            d["Orders"] = ast.literal_eval(d["Orders"])
        order_operations_menu(products_list, orders_list, couriers_list)
    elif usr_input == 3:
        # Option 3: Couriers Operations Menu
        couriers_list = read_list_of_dicts_from_csv("./data/couriers_list.csv")
        # Due to a list being stored in the value of key: Orders inside couriers_list
        # We need to execute an operation to convert each value upon read to enable list operations
        # Will this break them? Maybe we convert when run?
        for d in couriers_list:
            d["Orders"] = ast.literal_eval(d["Orders"])
        courier_operations_menu(couriers_list)
    else:
        # Input Invalid / Out of range
        os.system("cls||clear")
        print(
            "Invalid Input Option, please select an integer from the Options Listed: "
        )
        main_options_menu()


if __name__ == "__main__":
    main_options_menu()
