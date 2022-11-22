# Creating a Tableusing PyMySQL
# MY SQL Syntax:
# CREATE TABLE table_name(
#     column1 datatype, 
#     column2 datatype, 
#     column3 datatype,
#     column4 datatype,
# );
# To do these commands we need to use a mysql connector:
# import mysql.connector
# # Template: Create a connection:
# mydb = mysql.connector.connect(
# host = "localhost", 
# user = "yourusername",
# password="yourpassword"
# )

# print(mydb)

# # Template: Create a Database:
# mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE mydatabase")
# # Print list of databases:

# Example to match https://mothishdeenadayalan.medium.com/containerizing-a-python-app-mysql-python-docker-1ce64e444ed9
import mysql.connector
import tabulate
from mysql.connector import errorcode
from err_catching_helper_functions import *
def open_connection_wrapper():
    try:
        cnx = mysql.connector.connect(user='root',
                                    host='mydb',
                                    password='root', 
                                    port = 3306)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        print(f"Hello we managed to open the connection {cnx}")
        return(cnx)

def get_sql_database_names(sql_cursor):
    # Requires open connection and mysql cursor object
    # Returns list of database names
    sql_cursor.execute("SHOW DATABASES")
    db_names = [item[0] for item in sql_cursor]
    print(db_names)
    return(db_names)

def get_sql_table_names(sql_cursor):
    # Requires open connection and mysql cursor object
    # Returns list of database table names
    sql_cursor.execute("SHOW TABLES")
    table_names = [item[0] for item in sql_cursor]
    print(table_names)
    return(table_names)

def create_sql_table(sql_cursor, table_name:str, col_names:list, col_dtypes:list):
    sql_cursor.execute(f"CREATE TABLE {table_name} (id INT AUTO_INCREMENT PRIMARY KEY)")
    # Add Some Columns
    for tup in zip(col_names, col_dtypes):
        print(tup[0], tup[1])

def get_sql_col_names(sql_cursor, table_name):
    # Requires open connection and mysql cursor object + valid table_name
    # Returns list of column names in table
    sql_cursor.execute(f"SHOW COLUMNS FROM {table_name}")
    column_names = [item[0] for item in curse]
    print(column_names)
    return(column_names)

def get_sql_col_dtypes(sql_cursor, table_name):
    # Requires open connection and mysql cursor object + valid table_name
    # Returns list of column names in table
    sql_cursor.execute(f"SHOW COLUMNS FROM {table_name}")
    dtypes = [item[1] for item in curse]
    print(dtypes)
    return(dtypes)

def add_row_to_table(connection, sql_cursor, table_name):
    # Function to add a row to a table based on user input and commit changes
    col_names = get_sql_col_names(sql_cursor, table_name)
    dtypes = get_sql_col_dtypes(sql_cursor, table_name)
    val = []
    # Iterate over column names for inputs
    for col,dtype in zip(col_names, dtypes): 
        new_var = input(f"Enter a new value for {col} (with type {dtype}) : ")
        val.append(new_var)
    # Strip and format the command
    col_names_fmt = str([str(item) for item in col_names])
    val_fmt = str([str(item) for item in val])
    # Remove brackets (and apostrophes from col_names)
    col_names_fmt = col_names_fmt.lstrip("[").rstrip("]")
    col_names_fmt = col_names_fmt.replace("'", "")
    print(col_names_fmt)
    val_fmt = val_fmt.lstrip("[").rstrip("]")
    print(val_fmt)
    # CREATE INSERT INTO COMMAND
    sql_command = f"INSERT INTO {table_name} ({col_names_fmt}) VALUES ({val_fmt})"
    # Run Command
    sql_cursor.execute(sql_command)
    connection.commit()

def remove_row_from_table(connection, sql_cursor, table_name):
    # Function to remove a row from a table
    pass

def print_sql_table(sql_cursor, table_name):
    # requires tabulate: https://pypi.org/project/tabulate/
    # Prints formatted table from MySql Table using Tabulate Package
    # Args: 
    # sql_cursor, mysql.connector cursor object pointed at a database
    # Name of Table to print
    col_names = get_sql_col_names(sql_cursor, table_name)
    sql_cursor.execute(f"SELECT * FROM {table_name}")
    result = sql_cursor.fetchall()
    print(tabulate.tabulate(result, headers=col_names, tablefmt='psql'))

# Command examples:
# CREATE DATABASE <db_name>
# USE <db_name>
# SHOW DATABASES
# SHOW TABLES
# CREATE TABLE play_table (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))
# ALTER TABLE play_table ADD COLUMN tel VARCHAR(255)
# Add rows to a table:
# INSERT INTO <table> (<col1>, <col2>) VALUES (<val1>, <val2>)
# Commit Changes:
# db.commit()
# print(mycursor.rowcount, "record inserted.")


# Attempt to Open The Connection:
con_air = open_connection_wrapper()
# Create A cursor:
curse = con_air.cursor(buffered=True)
# Retrieve Database Names
curse.execute("SHOW DATABASES")
db_names = [item[0] for item in curse]
# Verify Desired Operations Database contained in MySQL Database, Create and Use the database
db_name = "db_playground"
if db_name in db_names:
    print("The Database exists inside the MySQL Database")
    # Use The database
    curse.execute("USE db_playground")
else:
    print("Nada")
    print("The database doesn't exist we need to create it")
    usr_create = get_min_length_string(f"Would you like to create the database {db_name}? (y/n): ")
    if usr_create.lower() == "y":
        curse.execute(f"CREATE DATABASE {db_name}")
        curse.execute(f"USE {db_name}")
    else:
        print("User Selected Not to Create a Database")
# Print the Database Tables
# PRint the Tables belonging to the database
print("The Tables inside this Database are:")
curse.execute("SHOW TABLES")
table_names = [item[0] for item in curse]
if len(table_names) == 0:
    print(f"There are no Tables in the Database {db_name}")
    usr_create = get_min_length_string("Would you like to create a Table? (y/n): ")
    if usr_create.lower() == "y":
        table_name = "Products"
        col1 = ("id", "INT AUTO_INCREMENT PRIMARY KEY")
        col2 = ("name", "VARCHAR(255)")
        col3 = ("price", "VARCHAR(255)")
        curse.execute(f"CREATE TABLE {table_name} ({col1[0]} {col1[1]}, {col2[0]} {col2[1]}, {col3[0]} {col3[1]})")
else:
    for i, table in enumerate(table_names):
        print(f"{i} = {table}")
    pick_table = get_min_length_string("Select Table from above options to start playing with")

# Temp file 1:
# Create some tables fro templates:
if "products" not in table_names:
    curse.execute("CREATE TABLE products (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), price DECIMAL(10,2))")
    curse.execute("INSERT INTO products (name, price) VALUES ('chocolate', 0.99);")
if "orders" not in table_names:
    curse.execute("CREATE TABLE orders (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255), tel VARCHAR(15), status VARCHAR(15), time DATE, items VARCHAR(255), courier_id INT)")
    curse.execute("INSERT INTO orders (name, address, tel, status, time, items, courier_id) VALUES ('Tim', 'Here', '0800001066', 'preparing', 2022-11-21,'[chocolate, banana]', '1');")
if "couriers" not in table_names:
    curse.execute("CREATE TABLE couriers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), tel VARCHAR(15), order_ids VARCHAR(255))")
    curse.execute("INSERT INTO couriers (name, tel, order_ids) VALUES ('courier_pete', '0800118118', '1');")
# Temp file 2:
# Print the contents, column names etc of the tables for inspection
curse.execute("SHOW COLUMNS FROM products")
cols_products = [item[0] for item in curse]
curse.execute("SHOW COLUMNS FROM orders")
cols_orders = [item[0] for item in curse]
curse.execute("SHOW COLUMNS FROM couriers")
cols_couriers = [item[0] for item in curse]
print(cols_products)
print(cols_orders)
print(cols_couriers)
# Temp file 3:
# Make template operations to alter the code and operations
# * Note we may want to make one order item per product item request (3*banana + 4*chocolate) = 1 order, 2 order_items, 
def update_row_in_table(sql_cursor, table_name):
    # For an item in a table, retrieves the relevant index and mutates it as requested based on the inputs
    # Print Rows and ask user to pick the relevant row, grabs the id as a reference
    # for item in column names, ask if want to mutate and add to changes list variable
    # format strings and perform update operation
    pass

add_row_to_table(con_air, curse, "products")
print_sql_table(curse, "products")


# Rest Table names
curse.execute("SHOW TABLES")
table_names = [item[0] for item in curse]
    

dtype_string_mysql = (
    "CHAR(size)",
    "VARCHAR(size)",
    "BINARY(size)",
    "VARBINARY(size)",
    "TINYBLOB",
    "TINYTEXT",
    "TEXT(size)",
    "BLOB(size)",
    "MEDIUMTEXT ",
    "MEDIUMBLOB",
    "LONGTEXT",
    "LONGBLOB",
    "ENUM(val1, val2, val3, ...)",
    "SET(val1, val2, val3, ...)"
)
dtype_num_mysql = (
    "BIT(size) ",
    "TINYINT(size) ",
    "BOOL",
    "BOOLEAN",
    "SMALLINT(size)",
    "MEDIUMINT(size)",
    "INT(size)",
    "INTEGER(size)",
    "BIGINT(size)",
    "FLOAT(size, d)",
    "FLOAT(p)",
    "DOUBLE(size, d)",
    "DOUBLE PRECISION(size, d)",
    "DECIMAL(size, d)",
    "DEC(size, d)"
)
dtype_time = (
    "DATE",
    "DATETIME(fsp)",
    "TIMESTAMP(fsp)",
    "TIME(fsp)",
    "YEAR"
)


print(table_names)
chosen_table_id = options_selector(table_names,"Pick a table you schmuck")
A = 1/0
# Select a Table to work with:
# Create DB Connection assuming docker all set up
cnx = mysql.connector.connect(host = 'mydb', user = 'root', password = 'root', port = 3306, database='db_playground')
print(cnx)
# Ok Now we need to create a database + tables
mycursor = cnx.cursor()
huh = mycursor.execute("SHOW DATABASES")
print(type(mycursor))
for item in mycursor:
    print(item)
# Now we need to look inside the Databases in mycursor and check if the one we wish to use/create already exists
print("\n\n\n\n")
print(mycursor)
db_names = [item for item in huh]
print(db_names)
if "db_playground" in db_names:
    print("The Database already exists")
else:
    print("The database doesn't exist")
A = 1/0
if not True:
    mycursor.execute("CREATE DATABASE db_playground")
# Let's print the list of databases:
mycursor.execute("SHOW DATABASES")
for item in mycursor:
    print(item)
mycursor.execute("USE db_playground")
# Create A Table:
mycursor.execute("CREATE TABLE play_table (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
print("46".center(50, "/"))
# Print list of tables
mycursor.execute("SHOW TABLES")
print("49".center(50, "/"))
for x in mycursor:
    print(x)
# If the table already exists, use ALTER:
print("53".center(50, "/"))
mycursor.execute("ALTER TABLE play_table ADD COLUMN tel VARCHAR(255)")
print("55".center(50, "/"))

print("It was on a cold dark night, born into this world")
print("They didn't know back then")
cnx.close()
# docker-compose up -d
# docker-compose build <yml-service-name>
# docker-compose run <yml-service-name>
# https://mothishdeenadayalan.medium.com/containerizing-a-python-app-mysql-python-docker-1ce64e444ed9
# https://www.dabbleofdevops.com/blog/setup-a-mysql-python-docker-dev-stack
# https://blog.carlesmateo.com/2021/07/07/a-small-python-mysql-docker-program-as-a-sample/
# https://docs.docker.com/engine/reference/builder/