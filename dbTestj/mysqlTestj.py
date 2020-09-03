import mysql.connector

## Connecting to the database

## connecting to the database using 'connect()' method
## it takes 3 required parameters 'host', 'user', 'passwd'
cnx = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "mysqlrootaccountpwj"
)

print('j) cnx:',cnx) # it will print a connection object if everything is fine

cursor = cnx.cursor()

## executing the statement using 'execute()' method
cursor.execute("show databases")

## 'fetchall()' method fetches all the rows from the last executed statement
databases = cursor.fetchall() ## it returns a list of all databases present

## printing the list of databases
print(databases)

## showing one by one database
for database in databases:
    print(database)

cursor.close()
cnx.close()