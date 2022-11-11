# Area for making dummy functions before implementation
# Make a list of dictionaries and save to line delimited csv file
# Reload the list of dictionaries from the line delimited csv file
from datetime import datetime
from fileHandler_helper_functions import *
order_i = ["Chocolate", "Chicken"]
order_q = [1,2]
order_t = str(datetime.today().strftime('%Y-%m-%d'))
# Make some product dicts
product1 = {"Name": "Chocolate", "Price": 0.85}
product2 = {"Name": "Chicken", "Price": 1.25}

# make some order dicts
order1 = {"Name":"Adam", "Address":"Adam House" , "Tel":"01204ADAM" , "Items":{"I": order_i, "Q": order_q}, "Time":order_t, "Status":"preparing",  "Order_ID":"Adam_001" , "Courier":"Zebra"}
order2 = {"Name":"Ben", "Address":"Ben House" , "Tel":"01204BENJ" , "Items":{"I": order_i, "Q": order_q}, "Time":order_t, "Status":"preparing",  "Order_ID":"Benj_001" , "Courier":"Yak"}
order3 = {"Name":"Charlie", "Address":"Charlie House" , "Tel":"01204CHAZ" , "Items":{"I": order_i, "Q": order_q}, "Time":order_t, "Status":"preparing",  "Order_ID":"Chaz_001" , "Courier":"Xylophone"}

# make products, orders into lists of dicts
list_of_orders = [order1, order2, order3]
list_of_products = [product1, product2]

# Now let's try to save these to a csv based on the internet:
keys = list_of_products[0].keys()

# def save_list_of_dicts_to_csv(list_of_dicts, filepath):
#     # Function to save a list of Dictionaries to a csv
#     # Requires all dictionaries in list to have identical keys and orders
#     # Args:
#     # list_of_dicts = list of dictionaries, all keys must be the same
#     # filepath = str, full name of file.csv to be saved
#     keys = list_of_dicts[0].keys()
#     with open(filepath, 'w+', newline='') as f:
#         dict_writer = csv.DictWriter(f, keys)
#         dict_writer.writeheader()
#         dict_writer.writerows(list_of_dicts)

# def read_list_of_dicts_from_csv(filename):
#     # Function to read a list of Dictionaries from a csv
#     # Assumed all dictionaries in list to have identical keys and orders
#     # Args:
#     # filename = string, full path to csv file
#     with open(filename, 'r') as f:
#         reader = csv.DictReader(f)
#         list_of_dicts = [dict for dict in reader]
#         return(list_of_dicts)

readin = read_list_of_dicts_from_csv("dummy_products.csv")
print(readin)
# Now we have the new format for the products, we should see how the functions respond to the new data type?
