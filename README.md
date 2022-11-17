# Bookish-Succotash
A Cafe Order Menu System for managing products, couriers and orders in a CLI interface using Python.
Client Requirements included:
- CLI navigable main menu to reach submenus for Products, Order and Courier operations
- Ability to print, add, update/amend and remove: Products, Orders, Couriers
- Commit data structures containing Product, Order and Courier information to files
- Products Attributes include: Name, Price
- Order Attributes include: Name, Address, Telephone, Items, Courier, Order Status, ID
- Courier Attributes include: Name, Orders

## Development
Initial client requirements built up from storing list of strings to text files to represent products, orders and couriers. Updating of these requirements provided the context for additional attributes, menu recursion and storing products as lists of dictionaries saved to CSV files.
The approach follows Functional Programming, with each menu and submenu housed in it's own def function wrapper with recursion to navigate between different menu functions.
Each menu function is supported by an array of helper functions as tabulated below:
<details>
<summary>Helper Functions</summary>

|  Name  | Purpose |Functionality |
|:------:|:-------:|:------------:|
|options_selector| Input Helper |List passed to function and printed with corresponding indices, returns user input to select corresponding option desired|
|get_non_neg_int| Error handling | user input function to restrict input to non-negative integers for use with options selection |
|get_non_neg_float| Error handling | user input function to restrict input to non-negative floats for e.g. Product price assignment |
|get_min_length_string| Error handling | user input function to restrict input strings within specified length ranges for e.g. Telephone no. and to avoid empty fields |
|save_list_of_dicts_to_csv| File handling | save list of dictionaries to CSV |
|read_list_of_dicts_from_csv| File handling | open and read list of dictionaries from CSV |
|string_representation_of_list_to_list| Read handling | Converts string representation of list to list object (workaround for CSV list of dictionary)* |
|make_string_unique| Duplicate Key avoidance | Returns a unique string by underscore and padded zeros ("_001") if string already exists in a given list |
|cafe_header| Decoration Helper | clears terminal and re-prints Cafe Welcome Message for use at all menu/sub-menu operations |
|print_list_of_dicts| Decoration Helper | Formatted Printing of a list of dictionaries using the Tabulate Module |
</details>

###### The smallest heading
Other stuff, can't believe you read this far..



Github repo
README.md
Project Background / Client requirements
How did you meet the client brief? (UNDERSTANDING CLIENT SPECIFICATION/REQUIREMENTS)
How did you guarantee the client requirements? (TESTING)
If you had more time, what is one thing you would improve upon? (ACTION PLAN FOR FUTURE IMPLEMENTATION)
What did you most enjoy implementing? (BANTS)
^ Structure of README
Presentation:
Show README
Present one core functionality
Will answer one question: testing, future implementing or enjoyed implementing
For Demo