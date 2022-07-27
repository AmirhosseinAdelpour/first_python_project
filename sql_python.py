# import mysql.connector
# from mysql.connector import connection
# import main_page





# def sqlInsert():
#     conn = mysql.connector.connect(
#     user = "pasha_adel",
#     passwd = "Amir09011597145",
#     host = "localhost",
#     database = "users")
#     cursorObject = conn.cursor()

#     sql = "INSERT INTO python_users ( name, phone_number, email, passwr) VALUES ( %s, %s, %s, %s)"
#     val = (main_page.Main_Page.db_name, main_page.Main_Page.db_phone_number, main_page.Main_Page.db_email, main_page.Main_Page.db_password)
#     cursorObject.execute(sql, val)
#     conn.commit()

# def printi():
#     print(type(main_page.Main_Page.db_name) ,  "sssssssssssss")
#     print(main_page.Main_Page.db_email , "salammmmmmm")

# # cursorObject.close()



