# # # Unique String Helper Functions:

def make_string_unique(s, list_s):
    # Function to convert an input string into a unique one
    # Performed by adding _ and max 3 padded 0's w/ iterative counter {num}
    # At 999 iterations exits and states not found
    # Args:
    # s = string(), word to be made unique
    # s_list = list of strings, list of strings to be unique from
    num = 1
    s = str(s)
    s += "_" + str(num).zfill(3)
    while (s in list_s) and (num < 999):
        num +=1
        s = s[:-3]
        s += str(num).zfill(3)
    return(s)