# import MySQLdb
import cgi
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
)

mycursor = mydb.cursor()
data=cgi.FieldStorage()
a=data.getvalue('e1')
b=data.getvalue('p1')

# mycursor.execute("CREATE DATABASE mydatabase")
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#   print(x)

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# # name = input("Enter name : ")
# # address=input("Enter address : ")
# val = (a, b)
# mycursor.execute(sql, val)
# mydb.commit()

# print(mycursor.rowcount, "record inserted.")
# mycursor.execute("SELECT * FROM customers")
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)

# sql = "SELECT * FROM customers WHERE address ='EKM'"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)

# sql = "DELETE FROM customers WHERE address = 'address'"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, "record(s) deleted")


# sql = "UPDATE customers SET address = 'Perumbavoor' WHERE address = 'EKM'"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, "record(s) affected")