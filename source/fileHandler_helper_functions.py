# FileHandler Operations Functions
import csv
# # # File Handler Helper Functions:
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


def save_list_of_dicts_to_csv(list_of_dicts, filepath):
    # Function to save a list of Dictionaries to a csv
    # Requires all dictionaries in list to have identical keys and orders
    # Args:
    # list_of_dicts = list of dictionaries, all keys must be the same
    # filepath = str, full name of file.csv to be saved
    keys = list_of_dicts[0].keys()
    with open(filepath, 'w+', newline='') as f:
        dict_writer = csv.DictWriter(f, keys)
        dict_writer.writeheader()
        dict_writer.writerows(list_of_dicts)


def read_list_of_dicts_from_csv(filename):
    # Function to read a list of Dictionaries from a csv
    # Assumed all dictionaries in list to have identical keys and orders
    # Args:
    # filename = string, full path to csv file
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        list_of_dicts = [dict for dict in reader]
        return(list_of_dicts)

