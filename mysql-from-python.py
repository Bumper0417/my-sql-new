import os 
import pymysql

# Get username from gitpod environment
# (Modify this variable if runnin on another environment)

username = os.getenv('C9_USER')

# Connect to the database
connection = pymysql.connect(host = 'localhost',
                            user = username,
                            password = '',
                            db = 'Chinook')
# Test
try:
    #Run a query
    with connection.cursor() as cursor:
        sql = "SELECT * from Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)

finally:
    # Close the connection, regardless of whether the above is correct
    connection.close()


