# Decoration and Print Operations Helper Functions
import os
import pyfiglet
import tabulate

def cafe_header():
    # Function to print presentation string
    # at top of menu calls
    os.system('cls||clear')
    print(pyfiglet.figlet_format("Dave's Cafe", font = "fuzzy" ))
    print(" Welcome ".center(50, '~'))
    print(" Dave's Cafe ".center(50, '~'))

def print_list_of_dicts(list_of_dicts):
    # requires tabulate: https://pypi.org/project/tabulate/
    # Prints formatted table from list of dictonary objects using tabulate package
    # Args: list_of_dicts = list of dictionaries
    try:
        headers = list_of_dicts[0].keys()
        rows = [dict_obj.values() for dict_obj in list_of_dicts]
        row_ids = [f"id = {id}" for id in range(len(rows))]
        print(tabulate.tabulate(rows, headers, showindex=row_ids))
    except IndexError as ide:
        print(f"Error: {ide}")
        print(f"Empty List argument in print_list_of_dicts(list_of_dicts)")
    pass
