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
from mysql.connector import errorcode
from err_catching_helper_functions import *
def open_connection_wrapper():
    try:
        cnx = mysql.connector.connect(user='root',
                                    database='db_playground', 
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

# Attempt to Open The Connection:
con_air = open_connection_wrapper()
# Create A cursor:
curse = con_air.cursor()
# Retrieve Database Names
curse.execute("SHOW DATABASES")
db_names = [item[0] for item in curse]
# Verify Desired Operations Database contained in MySQL Database
if "db_playground" in db_names:
    print("The Database exists inside the MySQL Database")
    # Use The database
    curse.execute("USE db_playground")
    # PRint the Tables belonging to the database
    print("The Tables inside this Database are:")
    curse.execute("SHOW TABLES")
    table_names = [item[0] for item in curse]
    print(table_names)
    chosen_table_id = options_selector(table_names,"Pick a table you schmuck")
else:
    print("Nada")
A = 1/0
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
    print("The dayabase doesn't exist")
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