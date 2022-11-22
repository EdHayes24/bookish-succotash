# Test Sorting a list of dicts by recursive keys:
from err_catching_helper_functions import options_selector
from decoration_helper_functions import print_list_of_dicts
d0 = {'Name': 'Tim Taylor', 'Address': "Tim's House", 'Tel': '232323', 'Items': {'Items': [{'Name': 'Chicken', 'Price': '1.0'}], 'Quantity': [5]}, 'Time': '2022-11-16', 'Status': 'Preparing', 'Order_ID': '2022-11-16_001_Tim_Taylor', 'Courier': {'Name': 'Courier_Pete', 'Tel': '123456789', 'Orders': ['2022-11-16_001_Tim_Taylor', '2022-11-16_002_Pete_Plywood']}}
d1 = {'Name': 'Pete Plywood', 'Address': 'Timber Avenue', 'Tel': '118118', 'Items': {'Items': [{'Name': 'Anthrax', 'Price': '2.0'}, {'Name': 'lollipops', 'Price': '3.0'}], 'Quantity': [3, 2]}, 'Time': '2022-11-16', 'Status': 'Preparing', 'Order_ID': '2022-11-16_002_Pete_Plywood', 'Courier': {'Name': 'Courier_Pete', 'Tel': '123456789', 'Orders': ['2022-11-16_001_Tim_Taylor', '2022-11-16_002_Pete_Plywood']}}        
d2 = {'Name': 'Timmy', 'Address': "Timmy's House", 'Tel': '7896545', 'Items': {'Items': [{'Name': 'Coca-Cola', 'Price': '4.0'}], 'Quantity': [5]}, 'Time': '2022-11-22', 'Status': 'Out-for-Delivery', 'Order_ID': '2022-11-22_003_Timmy', 'Courier': {'Name': 'Courier_Paul', 'Tel': '111666888', 'Orders': ['2022-11-22_003_Timmy']}}
lod = [d0, d1, d2]
print(lod)

def sort_list_of_dicts(list_of_dicts, key_to_sort_by):
    '''A function to return a sorted list of dictionaries'''
    # Function to sort a list of dictionaries by a column
    # 1: check data type associated with your key:
    d0 = list_of_dicts[0]
    dtype = type(d0[key_to_sort_by])
    if dtype in (str, int, float, complex):
        # Level 1 Sort, we can directly sort on these values with a lambda function
        ordered_dict = sorted(list_of_dicts, key=lambda x: x[key_to_sort_by])
        print_list_of_dicts(ordered_dict)
    elif dtype in (list, tuple, dict):
        # Level 2 Sort,
        # We need to do some extra work to sort by a subkey or sub index for these
        subkey=""
        ordered_dict = sorted(list_of_dicts, key = lambda x: x[key_to_sort_by][subkey])
    return ordered_dict

def recursive_items(dictionary):
    for key, value in dictionary.items():
        if type(value) is dict:
            yield from recursive_items(value)
        else:
            yield (key, value)

a = {'a': {1: {1: 2, 3: 4}, 2: {5: 6}}}

for key, value in recursive_items(lod[1]):
    print(key, value)

# if key_to_sort_by in ("Courier", "Items"):
#     list_of_subkeys = list(orders_list[0][key_to_sort_by].keys())
#     subkey = list_of_subkeys[
#         options_selector(
#             list_of_subkeys,
#             " Select Parameter to Sort by: ".center(50, " "),
#         )
#     ]
#     if subkey in ("Items"):
#         print_list_of_dicts(
#             sorted(
#                 orders_list,
#                 key=lambda x: x[key_to_sort_by][subkey][0]["Name"],
#             )
#         )
#     else:
#         print_list_of_dicts(
#             sorted(orders_list, key=lambda x: x[key_to_sort_by][subkey])
#         )
# else:
#     print_list_of_dicts(
#         sorted(orders_list, key=lambda x: x[key_to_sort_by])
#     )