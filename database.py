from connection import connect

def insert(sql,val):
    mydb= connect()
    mycursor= mydb.cursor()

    mycursor.execute(sql,val)

    mydb.commit()

    print(mycursor.rowcount,"Registo inserido.")
    print('Nome:',mycursor.lastrowid)

    mydb.close()

def select(sql):
    mydb = connect()
    mycursor = mydb.cursor()

    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    mydb.close()

    return myresult

def update(sql,val):
    mydb= connect()
    mycursor = mydb.cursor()

    mycursor.execute(sql,val)

    mydb.commit()

    print(mycursor.rowcount,'registro alterado.')

    mydb.close()