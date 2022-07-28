import mysql.connector
from mysql.connector import connection

def send_to_sql():
    global a
    # global name_insert, phone_number_insert, email_insert, password_insert
    conn = mysql.connector.connect(
    user = "pasha_adel",
    passwd = "Amir09011597145",
    host = "localhost",
    database = "users")
    cursorObject = conn.cursor()

    cursorObject.execute("SELECT * FROM python_users")
    result = cursorObject.fetchall()
    # conn.commit()
    b = []
    a = False
    for x in result:
        if x[3] == 'dfhui@maoil.com' and x[4] == '@Amir6626':
            a = True


send_to_sql()
if a == True:
    print("yes it is working...")
else:
    print("nooooo")

  





'@Amir6626', '09011597145', 'dfhui@mail.com', '@Amir6626'