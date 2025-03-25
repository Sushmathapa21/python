# import sqlite3
# conn = sqlite3.connect("mydatabase.db") #connects to a database.
# cursor = conn.cursor() #create a cursor object to execute SQl commands.
# #define table structure:
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS users(
#                id INTEGER PRIMARY KEY,
#                username TEXT NOT NULL, 
#                age INTEGER,
#                email TEXT UNIQUE
#                )
# ''')
# conn.commit() #commit the transactions

# #to insert a single record:
# import sqlite3
# conn = sqlite3.connect("mydatabase.db")
# cursor = conn.cursor()
# cursor.execute("INSERT INTO users(username, age, email)VALUES('Sushma', '21', 'sush@gmail.com')")
# conn.commit()

#to ask data from the user:
import sqlite3
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()
name = input("Enter the name: ")
age = int(input("Enter the age: "))
email = input("Enter the email: ")
cursor.executemany("INSERT INTO users (name, age, email) VALUES (?, ?, ?)", (name, age, email))
conn.commit()


name = input("enter the  name")
age = int(input("enter the  age"))
email = input("etner the email")
 
cursor.execute('INSERT INTO users (name, age, email) VALUES (?, ?, ?)', (name, age, email))
conn.commit()