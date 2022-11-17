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
db = mysql.connector.connect(host = 'mydb', user = 'root', password = 'root', port = 3306)
print(db)
print("DUDUDUDUDDUUDUDUDUDUDUDUDUUDUDUDUDUDUDUDUDUDUDDUDUDUDUDUDUDUDUDUDUDUDUDUD")
print("It was on a cold dark night, born into this world")
print("they couldn't tell back then, is it a boy or a girl?")
print("has since then been a story, of uncertainty")
print("It was claimed a child, that he would never be free")
print("Hey little world! you know what you're getting")
print("Oh please little world, It's kicking your head in")
print("What'cha gonna do? Anyone of you? What'cha gonna do when we come for you?")
print("Anyone of you? What'cha gonna do? What'cha gonna do when we come for you?")
print("Grow up advance to nothing")
print("Live in a house of clay")
print("He didn't know back then")
print("But they liked it that way")
print("He didn't do what they told him")
print("He never did what they said")
print("Try to tell him your wrong again and")
print("Is this what you get?")
print("Hey little world! you know what you're getting")
print("Oh please little world, It's kicking your head in")
print("What'cha gonna do? Anyone of you? What'cha gonna do when we come for you?")
print("Anyone of you? What'cha gonna do? What'cha gonna do when we come for you?")
print("Take it to your mother")
print("Now as the starlets are scraping")
print("Now he's as wide as the sea")
print("And when you look all around you")
print("He is what you see")
print("All around the bed")
print("He's gonna make sure you heard")
print("Hey little world! you know what you're getting")
print("Oh please little world, It's kicking your head in")
print("He's got them all lined up and they're ready to go")
print("They're all lined up and that's what he saw")
print("Hey little world, back in the ocean again")
print("What'cha gonna do? Anyone of you? What'cha gonna do when we come for you?")
print("Anyone of you? What'cha gonna do? What'cha gonna do when we come for you?")
print("What'cha gonna do? Anyone of you? What'cha gonna do when we come for you?")
print("Anyone of you? What'cha gonna do? What'cha gonna do when we come for you?")
print("Hey little world! you know what you're getting")
print("Oh please little world, It's kicking your head in")
# docker-compose up -d
# docker-compose run <name in yml service>
# https://mothishdeenadayalan.medium.com/containerizing-a-python-app-mysql-python-docker-1ce64e444ed9
# https://www.dabbleofdevops.com/blog/setup-a-mysql-python-docker-dev-stack
# https://blog.carlesmateo.com/2021/07/07/a-small-python-mysql-docker-program-as-a-sample/
# https://docs.docker.com/engine/reference/builder/