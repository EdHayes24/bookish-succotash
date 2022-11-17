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
Initial client requirements have been built up from products, couriers and orders represented by lists of strings saved to *.txt files, to representation using lists of dictionaries stored in csv files. Updates to the requirements provided the context for additional attributes, menu recursion and new r/w protocols. Additional Stretch and Bonus features fulfilled include:
- Sorting of Orders List by all attributes
- Menu Recursion
- Deletion, Updates, Addition for all object types
To achieve this, the approach follows Functional Programming, with each menu and submenu housed in it's own def function wrapper with recursion to navigate between different menu functions.
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

## Additional Features
In addition to the bonus features, additional features including:
- Sort printed Orders by any attribute
- Orders Contain Time of order attribute and Unique Identifier Strings for eventual database storage
- Product, Courier and Order attribute fields checked for duplicate naming on addition/updating
- Enforced recursion with try exception to only accept valid entries (e.g. integer within range, minimum n characters for name/address etc..)
- Pyfiglet decoration strings in menu headers
- Tuples used to store expected dictionary keys, menu options and more to help prevent abuse by mutation.
## Bugs and Room for Improvement
While these features have been successful, there are some things which could be improved:
1. A previous feature used shallow and deep copies to permit user to keep or discard changes mutating a copy before commiting to a variable and finally a file upon menu exit. For large objects this process could become unwieldly and introduces confusion into the code. Rollbacks should be implemented a different way.
2. To improve performance, a decision was taken to mutate Product/Order/Courier data structures inside each sub-menu, only saving the changes to the file when the relevant operation had succeeded and the user selected to exit the current menu. On re-entry (e.g.from products_menu>main>products_menu), the file is reloaded in the main menu function before re-entry. This means that if an error/crash were to occur in the sub-menu, the most recent change AND any previous changes made to the data structure wouldn't be saved, invalidating ACID transactions. 
3. Files are currently completely overwritten on save operations using the w+ command, this is likely bad practice w.r.t the ACID transactions discussed prior.
4. SOLID + FP upon embarking on the constantly changing needs of the client, functional programming for many different menu functions could become untenable with each data structure having slightly different requirements. A more SOLID and easily maintained approach may be achieved using OOP but this would also require a large amount of refactoring. The large functional dependencies also inhibits ease of testing.
Additional Bugs to be resolved include:
1. Order_IDs which contain the Name of the Orderer aren't currently updated with the Order Name updates which could be confusing.
2. CSV read error* (list of dictionaries, one dict_value contains list which is interpreted as a literal string upon csv.DictRead() operation) is resolved by an ugly patch, a better solution is required. 

## Testing
Tests have been written for Error Handling Helper functions at this stage using a monkey patch to replace user inputs with strings which should invalidate a test. The recursive nature of these helper functions helps testing that the assertion is only reached for the final monkeypatch valid input after a series of invalid ones. The tests could be improved for catching non-string entry to the input() argument to prevent abuse by injection. 

Manual Usage has formed the main other type of testing, with codified testing in the pipeline for all helper functions.
## Enjoyable things and Hindsight Programming...
I most enjoyed the coding of the options_selector() and error handling helper functions as they are repeatedly useful sections of code within the project forming the basis of most user input operations to navigate the CLI menus - without which the other operations would be meaningless. By using tuples to store menu options and expected dictionary keys, the risk of mutation and errors occurring has been significantly reduced.

If I had my time again, and knew more about the eventual structure of the program and required features, I would start with an OOP approach using functions for generic helpers and specific methods for each data structure instead.