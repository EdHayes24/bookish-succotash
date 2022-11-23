# err_catching_helper_functions.py
# Python File containing helper functions for standardised recursive error catching functions for user input
"""
err_catching_helper_functions.py
"""
# Input Error Catching Functions
def get_non_negative_int(prompt: str):
    '''
    Retrieve user input of type integer > 0 based on string prompt.\n
    While loop used to recursively get new entry if the input doesn't meet the type requirements.
    '''
    while True:
        try:
            value = input(prompt)
            if "." in value:
                raise ValueError(
                    "Error: . character detected, Floats not permitted. Please enter an integer value"
                )
            value = int(value)
        except ValueError as ve:
            print(f"Error: {ve}\n Please enter a positive integer value")
            continue

        if value < 0:
            print("Sorry, your response must not be negative.")
            continue
        else:
            break
    return value


def get_min_length_string(prompt, length_min=1, length_max=255):
    '''
    Retrieve user input string length > 0 based on string prompt.\n
    While loop used to recursively get new entry if the input doesn't meet the type requirements.
    '''
    while True:
        s = input(prompt)
        if len(s) < length_min:
            print(f"***Please enter a String with length greater than {length_min} :")
            continue
        elif len(s) > length_max:
            print(
                f"***Please enter a String with length in range: {length_min} < s < {length_max} :"
            )
            continue
        else:
            break
    return s


# Input Error Catching Functions
def get_non_neg_float(prompt):
    '''
    Retrieve user input of type float > 0 based on string prompt.\n
    While loop used to recursively get new entry if the input doesn't meet the type requirements.
    '''
    while True:
        try:
            value = float(input(prompt))
        except ValueError as ve:
            print(f"Error: {ve}\n Please enter a positive float value")
            continue

        if value < 0:
            print("Sorry, your response must not be negative.")
            continue
        else:
            break
    return value


# # # User Input Helper Functions:
def options_selector(options_list, message="\n", err_msg="\n"):
    '''Prints options_list and assigns indices + requests user input to select option.\n
    Recursively executes until valid input recieved with updated err_msg. \nReturns usr input index.'''
    # Function to ask user to choose an option from the printed list
    # Args:
    # options = list or tuple, list of options to choose from
    # message = string, printed sub-menu header
    # err_msg = string, informs user of correct input format based on prior error
    print(message)
    print(err_msg)
    for i, option in enumerate(options_list):
        print(f"{i} = {option}")
    try:
        choice = get_non_negative_int("Please Enter the ID of the desired Option: ")
        # choice = int(input("Please Enter the ID of the desired Option: "))
        print(f"You have selected: {options_list[choice]}")
    except IndexError as ide:
        print(f"Error {ide} ")
        err_msg = f"*** Please enter an integer value within {range(len(options_list))}"
        choice = options_selector(options_list, message, err_msg)
        return choice
    except Exception as e:
        print(f"Error {e} ")
        err_msg = "*** Please enter an integer corresponding to the desired options:"
        choice = options_selector(options_list, message, err_msg)
        return choice
    else:
        return choice
