import mysql.connector

def connect():
    mydb = mysql.connector.connect(
    host="localhost",
    user="Eduardo",
    password="eduardo.1",
    database="hotel"
)

    return mydb