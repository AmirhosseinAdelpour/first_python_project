import mysql.connector
from mysql.connector import connection

def get_from_db():
    global a
    # global name_insert, phone_number_insert, email_insert, password_insert
    conn = mysql.connector.connect(
    user = "pasha_adel",
    passwd = "Amir09011597145",
    host = "localhost",
    database = "users")
    cursorObject = conn.cursor()

    cursorObject.execute("SELECT email, passwr FROM python_users")
    result = cursorObject.fetchall()
    # conn.commit()
    b = []
    a = False
    name = ('rtdstsd@gmail.com', '@aMIR6626')
    for x in result:
        b.append(x)
    if name in b:
        print("yes")


get_from_db()

  


