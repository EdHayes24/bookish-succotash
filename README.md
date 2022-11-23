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
|products_selector_add| Products Selector | Gets user input to add multiple products to an order, quantity updated only for selection of pre-existing items |
|products_selector_remove| Products Selector | Gets user input to remove products from an order|
|products_selector_amend| Products Selector | Alter products on an order |
|products_selector| Products Selector | User options selector to direct user to one of the above product_selector_* functions |
</details>

## Additional Features
In addition to the bonus features, additional features including:
- Permits Customer to add items and their quantities to an Order
- Sort printed Orders by any attribute
- Orders Contain DateTime of order attribute and Unique Identifier Strings for eventual database storage, (the second of which has become pointless for week5 data tables but nevermind)
- Product, Courier and Order attribute fields checked for duplicate naming on addition/updating
- Enforced recursion with try exception to only accept valid entries (e.g. integer within range, minimum n characters for name/address etc..)**this is also a problem...
- Pyfiglet decoration strings in menu headers
- Tuples used to store expected dictionary keys, menu options and more to help prevent abuse by mutation.
## Bugs and Room for Improvement
While these features have been successful, there are some things which could be improved:
1. A previous feature used shallow and deep copies to permit user to keep or discard changes mutating a copy before commiting to a variable and finally a file upon menu exit. For large objects this process could become unwieldly and introduces confusion into the code. Rollbacks should be implemented a different way, with the move towards MySql data tables, this will be corrected by use of database commit commands instead.
2. To improve performance, a decision was taken to mutate Product/Order/Courier data structures inside each sub-menu, only saving the changes to the file when the relevant operation had succeeded and the user selected to exit the current menu. Files are loaded once just prior to entry to the sub-menu. This means that if an error/crash were to occur in the sub-menu, the most recent change AND any previous changes made to the data structure wouldn't be saved, invalidating ACID transactions. 
3. Files are currently completely overwritten on save operations using the w+ command, this is likely bad practice w.r.t the ACID transactions discussed prior.
4. SOLID + FP upon embarking on the constantly changing needs of the client, functional programming for many different menu functions could become untenable with each data structure having slightly different requirements. A more SOLID and easily maintained approach may be achieved using OOP but this would also require a large amount of refactoring. The large functional dependencies also inhibits ease of testing. A lesson has been learned in the maintenance cost of programming
5. Functions betray single responsibility protocols in many areas of the program making it difficult to test. In other cases, self contained recursion in functions (e.g. those in err_handling_helper_functions.py**) make program breaking errors if conditions are not met. It would be better to deal with input recursion errors outside of the functions themselves to avoid these breaking errors which have to be bodged around. This is further evidenced by repeated return and function calls in try-except blocks inside a function. A better example and approach has been implemented in the product_selector suite of functions w.r.t single responsibility and the database table operations currently under development. It is also clear in some menu functions where complicated hard coded solutions exist.


Additional Bugs to be resolved include:
1. User is permitted to enter 0 quantity for a product
2. Structure of Order Dictionary under the key of "Items" is messy, causing issues with sort arguments requiring aformentioned hard coded solution
3. 
4. CSV read error* (list of dictionaries, one dict_value contains list which is interpreted as a literal string upon csv.DictRead() operation) is resolved by an ugly patch, a better solution is required. 

## Testing
Tests have been written for Error Handling Helper functions at this stage using a monkey patch to replace user inputs with strings which should invalidate a test. The recursive nature of these helper functions helps testing that the assertion is only reached for the final monkeypatch valid input after a series of invalid ones. The tests could be improved for catching non-string entry to the input() argument to prevent abuse by injection. 

Testing of the unique_str_helper_functions.py has been performed without any mocking opr patching. These remain concepts with which I am yet to gain a firm grasp on using without the context of OOP, for FP they make less sense to me. 

Manual Usage has formed the main other type of testing, with codified testing subject of future work after significant refactoring has been completed to facilitate such testing.
## Enjoyable things and Hindsight Programming...
I most enjoyed the coding of the options_selector() and error handling helper functions as they are repeatedly useful sections of code within the project forming the basis of most user input operations to navigate the CLI menus - without which the other operations would be meaningless. By using tuples to store menu options and expected dictionary keys, the risk of mutation and errors occurring has been significantly reduced and their repeated use has meant a more standardised view of the respective menu and sub-menu systems.

I was also enjoying interacting and setting up databases with a dockerised python app which I have set up from writing YML and dockerfile to do so - this was a complicated aspect for me to learn how to make linked databases with a built application, but it has opened my eyes to additional possibilities using docker in this manner. I feel that the self-critique of my program and my venture into creating docker builtapps+databases will be some of the most valuable lessons I take from this mini project to date.    

If I had my time again, and knew more about the eventual structure of the program and required features, I would start with an OOP approach using functions for generic helpers and specific methods for each data structure instead. With respect to the FP approach I applied, I would refactor to provide more single-objective functions in the program which in turn should help with translation to OOP methods, dataclasses and composition (attempting to avoid inheritance coupling issues).