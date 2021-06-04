import mysql.connector

mydb = mysql.connector.connect(
    host="",
    user="",
    password="",
    database=""
)

print("please enter your email:")
email = input()

print("please enter your password:")
password = input()


mycursor = mydb.cursor()
sql = "INSERT INTO info (Emails, PASSWORDS) VALUES (%s, %s)"
val = (email, password)
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record insterted.")