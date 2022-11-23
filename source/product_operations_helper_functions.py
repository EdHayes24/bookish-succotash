# product_operations_helper_functions.py
# Python File containing helper functions for products
# Includes wrapper function, add, remove, print and update
"""
product_operations_helper_functions.py
"""
from err_catching_helper_functions import options_selector, get_non_negative_int


def products_list_add(products_list, item):
    '''
    Appends item to list only if the item isn't in the list already
    '''
    # Function to add an item to update/add an item to the products list
    # Args:
    # products_list = list of strings, current products_list to be updated
    # item = string, item to be added to product list
    if item in products_list:
        print(f"Item {item} is already in the products_list product list")
        print("Aborting products_list_add() operation")
    else:
        products_list.append(item)
    return products_list


def product_selector_add(items_list:list, out_dict:dict, key_names=("Items", "Quantity")):
    '''
    Recursively gets user input for product to add to an order dictionary until user chooses to stop.\n
    If product already in order, increments quantity instead.
    Returns updated order dictionary
    '''
    # Function to obtain user input for order choice
    carryOn = True
    while carryOn:
        pick = options_selector(items_list, "Please select the desired product: ")
        chosen_item = items_list[pick]
        quantity = get_non_negative_int(
            f"Enter quantity of {items_list[pick]} desired: "
        )
        prior_items = out_dict.get(key_names[0])
        if chosen_item in prior_items:
            # Item exists, add to quantity in corresponding index instead
            print(f"Item {chosen_item} has already been selected")
            idx = prior_items.index(chosen_item)
            existing_quantity = out_dict.get(key_names[1])[idx]
            print(
                f"Adding {quantity} to existing total {existing_quantity} = {quantity+existing_quantity}"
            )
            out_dict[key_names[1]][idx] = quantity + existing_quantity
        else:
            out_dict[key_names[0]].append(chosen_item)
            out_dict[key_names[1]].append(quantity)
        usr_continue = input("Add another item? (y/n): ")
        if usr_continue.lower() != "y":
            carryOn = False
    return out_dict


def product_selector_remove(out_dict, key_names=("Items", "Quantity")):
    '''
    Recursively gets user input for product to remove to an order dictionary until user chooses to stop.\n
    If the order dictionary is empty, returns the last modified version before attempting a removal. 
    Returns updated order dictionary
    '''
    # Function to obtain user input for order item removal
    carryOn = True
    while carryOn:
        if not out_dict[key_names[0]]:
            # Empty Dictionaries evaluate to False
            # Dictionary empty, abort removal
            print(f"Nothing to remove from {out_dict}")
            print("Aborting removal operation")
            carryOn = False
        else:
            pick = options_selector(
                out_dict.get(key_names[0]), "Please select the product to remove: "
            )
            print(out_dict)
            for key in key_names:
                del out_dict[key][pick]
            usr_continue = input("Remove another item? (y/n): ")
            if usr_continue.lower() != "y":
                carryOn = False
    return out_dict


def product_selector_amend(out_dict, key_names=("Items", "Quantity")):
    '''
    Recursively gets user input for product to amend and new quantity to update order dictionary until user chooses to stop.\n
    Returns updated order dictionary
    '''
    # Function to obtain user input for order item quantity amendment choice
    carryOn = True
    while carryOn:
        pick = options_selector(
            out_dict.get(key_names[0]), "Please select the product to amend: "
        )
        print(f"Quantity: {out_dict[key_names[1]][pick]}")
        quantity = get_non_negative_int(
            f"Enter New quantity of {out_dict.get(key_names[0])[pick]} desired: "
        )
        out_dict[key_names[1]][pick] = quantity
        usr_continue = input("Amend another item? (y/n): ")
        if usr_continue.lower() != "y":
            carryOn = False
    return out_dict


def product_selector(option:int, items_list, dict_out, key_names=("Items", "Quantity")):
    '''
    Product Selection Operations Mini Menu for alterations to items on an order dictionary\n
    Returns unaltered order dictionary for option out of range\n
    Returns updated order dictionary based on optional function.
    '''
    if option == 0:
        # Cancel, abort operation
        print("Abort Product Select Operation Menu")
    elif option == 1:
        # Add to items to order
        dict_out = product_selector_add(items_list, dict_out, key_names)
    elif option == 2:
        # Remove items from order
        dict_out = product_selector_remove(dict_out, key_names)
    elif option == 3:
        # Amend Count of an item
        dict_out = product_selector_amend(dict_out, key_names)
    else:
        # Out of range, abort
        print("Index not in range, aborting product_selector operation")
    return dict_out
