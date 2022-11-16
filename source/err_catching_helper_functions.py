# Input Error Catching Functions
def get_non_negative_int(prompt):
    while True:
        try:
            value = input(prompt)
            if "." in value:
                raise ValueError("Error: . character detected, Floats not permitted. Please enter an integer value")
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

def get_min_length_string(prompt, length_min=1, length_max = 255):
    while True:
        s = input(prompt)
        if len(s) < length_min:
            print(f"***Please enter a String with length greater than {length_min} :")
            continue
        elif len(s) > length_max:
            print(f"***Please enter a String with length in range: {length_min} < s < {length_max} :")
            continue
        else:
            break
    return s


# Input Error Catching Functions
def get_non_neg_float(prompt, dp=None):
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
