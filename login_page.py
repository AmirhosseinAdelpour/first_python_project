from tkinter import *
import random
from tkinter.font import BOLD
import captcha
from captcha.image import ImageCaptcha
from PIL import ImageTk, Image
import datetime

from requests import delete
import restore_password_validation as rpv
import mysql.connector
from mysql.connector import connection
from tkinter import messagebox
import re

class Login:

    def __init__(self):
        # app setting

        login_root = Tk()
        login_root.title("Login")
        login_root.geometry("500x560")
        login_root.resizable(False, False)
        app_icon = PhotoImage(file="app-icon.jpg")
        login_root.iconphoto(False, app_icon)
        login_root.config(bg="white")

        
        # login lbl
        Label(login_root, text="login", font=("plain", 30, BOLD), bg="white").pack(pady=20)

        # email & password lbl & entry

        login_email_lbl = Label(login_root, text="Email", font="courier", bg="white")
        login_email_lbl.pack()

        login_email_entry = Entry(login_root, width=50, border=2, relief="ridge")
        login_email_entry.pack(pady=10)

        login_password_lbl = Label(login_root, text="password", font="courier", bg="white")
        login_password_lbl.pack()

        login_password_entry = Entry(login_root, width=50, show="*", border=2, relief="ridge")
        login_password_entry.pack(pady=10)


        # captcha

        def captcha_func():
            global captcha_txt, captcha_text, data_2, captcha_image, my_image,captcha_lbl
            captcha_text = str(random.randint(10000, 99999))
            captcha_txt = ""
            for item in captcha_text:
                captcha_txt += "  "
                captcha_txt += item
            
            captcha_image = ImageCaptcha()
            data_2 = captcha_image.generate(captcha_txt)
            captcha_image.write(captcha_txt, 'captcha_login.png')
            my_image = ImageTk.PhotoImage(Image.open("captcha_login.png"))

        captcha_func()

        captcha_lbl = Label(login_root, image=my_image)
        captcha_lbl.pack(pady=10)

        captcha_entry = Entry(login_root, width=25, border=2, relief="ridge")
        captcha_entry.pack()

        # change captcha

        def change_captcha():
            captcha_func()
            captcha_lbl.config(image=my_image)

        click_image = PhotoImage(file="test.png")

        recaptcha_btn = Button(login_root, width=30,height=30, image=click_image, command=change_captcha)
        recaptcha_btn.place(x=335, y=242)

        # regex

        login_email_regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


        def check_login_regex(email):
            if (re.search(login_email_regex, email)):
                return True
            else:
                return False



        # check email & password from database
        def check_email_password():
            global a
            conn = mysql.connector.connect(
            user = "pasha_adel",
            passwd = "Amir09011597145",
            host = "localhost",
            database = "users")
            cursorObject = conn.cursor()
            cursorObject.execute("SELECT email, passwr FROM python_users")
            result = cursorObject.fetchall()
            emails_and_passwords = []
            for items in result:
                emails_and_passwords.append(items)

            if len(login_email_entry.get()) == 0 or len(login_password_entry.get()) == 0:
                 messagebox.showerror("Unsuccessfull Try", "Please fill the blanks...!")             
            else:
                if check_login_regex(login_email_entry.get()):
                    user_info = (login_email_entry.get(), login_password_entry.get())
                    if user_info in emails_and_passwords:
                        if captcha_entry.get() == 0 or captcha_entry.get() != captcha_text:
                            messagebox.showerror("Captcha Error", "Wrong captcha!")
                            captcha_entry.delete(0, "end")
                        else:
                            messagebox.showinfo("Successfull Try", "You were successfully logged in (:")
                            login_email_entry.delete(0, "end")
                            login_password_entry.delete(0, "end")
                            captcha_entry.delete(0, "end")
                    else:
                        messagebox.showerror("Unsuccessfull Try", "Email or Password is wrong!!!")
                else:
                    messagebox.showerror("Invalid Email Error", "Please enter a valid email")



        # login btn

        login_btn = Button(login_root, text="Login", width=20, bd=5, relief="ridge", command=check_email_password)
        login_btn.pack(pady=20)

        #  forget_password_func

        def forget_password_func():
            login_root.destroy()
            rpv.Restore_Password_Validation()

        # forgot password

        forget_password_lbl = Label(login_root, text="Forgot your password?", font=("courier"), bg="white")
        forget_password_lbl.pack()

        forget_password_btn = Button(login_root, text="Click here", font=("courier", 8), fg="blue", cursor="hand2", bd=0,
        bg="white", command=forget_password_func)
        forget_password_btn.pack(pady=10)



        # time update  func

        def time_func():
            global time, time_date
            time = datetime.datetime.now()
            time_date = time.strftime("%H:%M:%S %p\n%Y/%m/%d")

            time_lbl.config(text=time_date)
            time_lbl.after(1000, time_func)

        # time & date lbls

        time = datetime.datetime.now()
        time_date = time.strftime("%H:%M:%S %p\n%Y/%m/%d")

        time_lbl = Label(login_root, text=time_date, font=("courier", 15), bg="white")
        time_lbl.pack(pady=20)


        time_func()
        login_root.mainloop()
        



if __name__ == "__main__":
        Login()