# unique_str_helper_functions.py
# Python File containing helper functions for modification of string
# to make string unique compared to remainder of list
"""
unique_str_helper_functions.py
"""

# # # Unique String Helper Functions:


def make_string_unique(s: str, list_s: list):
    '''Modifies input string s to make unique in list_s \n
    Performed by appending _ and zero padded number up to 999'''
    # Function to convert an input string into a unique one
    # Performed by adding _ and max 3 padded 0's w/ iterative counter {num}
    # At 999 iterations exits and states not found
    # Args:
    # s = string, word to be made unique
    # s_list = list of strings, list of strings to be unique from
    num = 1
    if (s in list_s):
        s = str(s)
        s += "_" + str(num).zfill(3)
    while (s in list_s) and (num < 999):
        num += 1
        s = s[:-3]
        s += str(num).zfill(3)
    return s
