# fileHandler_helper_functions.py
# Python File containing helper functions for open, read, write operations on files
# For standard variable formats (lists, list of dictionaries etc..)
# And standard data formats (.txt, .csv etc..)
"""
fileHandler_helper_functions.py
"""
import csv
from err_catching_helper_functions import get_min_length_string

# # # File Handler Helper Functions:
def commit_changes(original, updated):
    '''
    Function to request which argument to return (original/updated) \n
    Used to implement rollbacks for mutated shallow and deep copied variables
    '''
    # Function to decide whether or not to commit to changes
    # original = unedited value
    # updated = altered value
    # choice = Boolean from input , True if want to keep changes
    prompt = "Would you like to keep these changes? (y/n): "
    usr_input = get_min_length_string(prompt)
    # usr_input = input("Would you like to keep these changes? (y/n): ")
    choice = usr_input.lower()[0] == "y"
    if choice:
        return updated
    else:
        return original


def string_representation_of_list_to_list(list_as_string: str):
    '''
    Converts a string representation of a list ("[1,2,3,4]") into a python list object\n
    i.e. "[1,2,3,4]" -> ["1","2","3","4"]\n
    Developed due to csv.DictRead() generating string representation of list when reading\n
    dictionary value of list from a csv.
    '''
    # Function to convert a string representation of a python list object
    # Into a literal Python List
    # This can occur using csv.Dictreader where the value of a key contains a list object
    # Args:
    # list_as_string = str, e.g. "[1,2,3,4,'alphabetsoup', 24.3798]"
    # 1) Strip Square Brackets ton inspect inner string
    inner_string = list_as_string.strip("][")
    # 2) Check for any "," in string
    if "," in inner_string:
        # Multiple elements to split on
        list_obj = inner_string.split(",")
    else:
        list_obj = inner_string.split()
        # Just one to split on or none, remove white space
    # We now need to convert the contents to a given type we know of, e.g. integer, string, float, object
    return list_obj


def list_to_line_delim_txt(list_obj:list, filepath:str):
    '''
    Saves List object to line delimited text file - overwrites all file contents (w+)\n
    FileNotFoundErrors result in non-execution
    '''
    # Function to save a list of strings to a line delimited text file
    # Args:
    # list_obj = list to convert to string and save
    # filepath = string, with path to text file accesible from os.getcwd()
    try:
        with open(filepath, "w+") as f:
            list_obj = [str(item) for item in list_obj]
            f.write("\n".join(list_obj))
    except FileNotFoundError as fnfe:
        print(f"Error in: list_to_line_delim_txt({filepath})")
        print(f"Error: {fnfe}")
    except Exception as e:
        print(f"Error in: list_to_line_delim_txt({filepath})")
        print(f"Error: {e}")


def line_delim_txt_to_list(filepath: str):
    '''
    Reads line delimited text file to list object.\n
    Returns None for FileNotFoundError
    '''
    # Function to unpack a line delimited text file to a list of strings
    # Args: filepath = string with path to text file accesible from os.getcwd()
    # Returns: list of strings
    try:
        with open(filepath, "r") as f:
            out_list = []
            for line in f.readlines():
                out_list.append(line.strip("\n"))
    except FileNotFoundError as fnfe:
        print(f"Error in: line_delim_txt_to_list({filepath})")
        print(f"Error Type: {fnfe}")
        print("Returning None Object")
    except Exception as e:
        print(f"Error in: line_delim_txt_to_list({filepath})")
        print(f"Error Type: {e}")
        print("Returning None Object")
        return None
    else:
        return out_list


def save_list_of_dicts_to_csv(list_of_dicts: list, filepath: str):
    '''
    Saves List of dictionaries object to line delimited csv file with headers - overwrites all file contents (w+)\n
    Each Dictionary must have identical keys in the list
    '''
    # Function to save a list of Dictionaries to a csv
    # Requires all dictionaries in list to have identical keys and orders
    # Args:
    # list_of_dicts = list of dictionaries, all keys must be the same
    # filepath = str, full name of file.csv to be saved
    keys = list_of_dicts[0].keys()
    with open(filepath, "w+", newline="") as f:
        dict_writer = csv.DictWriter(f, keys)
        dict_writer.writeheader()
        dict_writer.writerows(list_of_dicts)


def read_list_of_dicts_from_csv(filename: str):
    '''
    Reads line delimited csv file to list of dictionaries object.\n
    ** if a dict value contains a list object, this will read function return a string representation of the list
    '''
    # Function to read a list of Dictionaries from a csv
    # Assumed all dictionaries in list to have identical keys and orders
    # Args:
    # filename = string, full path to csv file
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        list_of_dicts = [dict for dict in reader]
        return list_of_dicts
