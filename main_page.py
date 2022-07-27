from modulefinder import IMPORT_NAME
from tkinter import *
import random
from tkinter.font import BOLD
import datetime
import re
from tkinter import messagebox
import captcha
from captcha.image import ImageCaptcha
from PIL import ImageTk, Image
import email_verfication_send as evs
import mysql.connector
from mysql.connector import connection
import login_page
import email_verification_page




# app setting

class Main_Page:

    e_mail = ""

    db_name = ""
    db_phone_number = ""
    db_email = ""
    db_password = ""

    def __init__(self):

        win = Tk()
        win.title("Sign up")
        win.geometry("500x570")
        win.resizable(False, False)
        app_icon = PhotoImage(file="app-icon.jpg")
        win.iconphoto(False, app_icon)


        # head frame

        head_frame = Frame(win)
        head_frame.pack()

        entry_lbl = Label(head_frame, text="Sign Up", font=("plain", 30, BOLD))
        entry_lbl.pack(pady=20)

        # name lbl
        name_lbl = Label(head_frame, text="Name",  font=("courier, 10"))
        name_lbl.pack()

        name_input = Entry(head_frame, width=50)
        name_input.pack()

        # name validation

        def name_validation(name):
            if len(name) < 4 :
                return False
            else:
                return True

        # phone number

        phone_number = Label(head_frame,text="Phone number",  font=("courier, 10") )
        phone_number.pack()

        phone_number_input = Entry(head_frame, width=50)
        phone_number_input.pack()

        # phone number validation

        def phone_number_validation(phone):
            if len(phone) == 11:
                if phone[0] == "0" and phone[1] == "9":
                    return True
            else:
                return False


        # email & password

        email_input_lbl = Label(head_frame, text="Email", font=("courier, 10"))
        email_input_lbl.pack()
        email_input = Entry(head_frame, width=50)
        email_input.pack()

        password_lbl = Label(head_frame, text="Password", font=("courier, 10"))
        password_lbl.pack()

        password_input = Entry(head_frame, width=50, show="*")
        password_input.pack()

        password_confirm_lbl = Label(head_frame, text="Confirm Password", font=("courier, 10"))
        password_confirm_lbl.pack()

        password_confirm_input = Entry(head_frame, width=50, show="*")
        password_confirm_input.pack()

        # regex

        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


        def check(email):
            if (re.search(regex, email)):
                return True
            else:
                return False

        # captcha

        def captcha_func():
            global captcha_txt, captcha_text, data_1, captcha_image, my_image
            captcha_text = str(random.randint(10000, 99999))
            captcha_txt = ""
            for item in captcha_text:
                captcha_txt += "  "
                captcha_txt += item
            
            captcha_image = ImageCaptcha()
            data_1 = captcha_image.generate(captcha_txt)
            captcha_image.write(captcha_txt, 'captcha.png')
            my_image = ImageTk.PhotoImage(Image.open("captcha.png"))

        captcha_func()

        captcha_lbl = Label(head_frame, image=my_image)
        captcha_lbl.pack(pady=10)

        captcha_entry = Entry(head_frame)
        captcha_entry.pack()

        # recaptcha

        def change_captcha():
            captcha_func()
            captcha_lbl.config(image=my_image)

        click_image = PhotoImage(file="test.png")

        recaptcha_btn = Button(head_frame, width=30,height=30, image=click_image, command=change_captcha)
        recaptcha_btn.place(x=240, y=320)


        # password validation
        password_regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$"
        match_re = re.compile(password_regex)

        def send_to_sql():
            global name_insert, phone_number_insert, email_insert, password_insert
            conn = mysql.connector.connect(
            user = "pasha_adel",
            passwd = "Amir09011597145",
            host = "localhost",
            database = "users")
            cursorObject = conn.cursor()

            sql = "INSERT INTO python_users ( name, phone_number, email, passwr) VALUES ( %s, %s, %s, %s)"
            val = (Main_Page.db_name, Main_Page.db_phone_number,
            Main_Page.db_email, Main_Page.db_password)
            cursorObject.execute(sql, val)
            conn.commit()

        def pass_validation():
            global captcha
            if re.search(match_re, password_input.get()):
                if password_input.get() == password_confirm_input.get():
                    if captcha_entry.get() == captcha_text:

                        Main_Page.db_name += name_input.get()
                        Main_Page.db_phone_number += phone_number_input.get()
                        Main_Page.db_email += email_input.get()
                        Main_Page.db_password += password_input.get()

                        send_to_sql()

                        Main_Page.e_mail = email_input.get()
                        evs.Send_Email.user_email = Main_Page.e_mail
                        RUN3 = evs.Send_Email()

                        win.destroy()
                        run2 = email_verification_page.Email_Page()

                    else:
                        messagebox.showerror("captcha error", "Please fill the captcha blank to submit that you are not a bot!!")
                else:
                    messagebox.showerror("password confirmation error", "Password doesn't match!!")
            else:
                messagebox.showerror("password error", "Invalid password!!")

        # sign_up button func


        def sign_up():
            email = email_input.get()
            if len(name_input.get()) == 0 and len(phone_number_input.get()) == 0 and len(email_input.get()) == 0\
                and len(password_input.get()) == 0 and len(password_confirm_input.get()) == 0:
                messagebox.showerror("Emtry blanks!!"," please fill the blanks..!") 
            else:
                if name_validation(name_input.get()):
                    if phone_number_validation(phone_number_input.get()):
                        if check(email):
                            pass_validation()
                        else:
                            messagebox.showerror("email error", "wrong email!! try again")
                    else:
                        messagebox.showerror("Invalid number","Your phone number is invalid!!")
                else:
                    messagebox.showerror("Invalid name","Your name lengh should be more than 4 characters!!")



        # sign up button

        sign_up_btn = Button(head_frame, text="sign up", width=20, bd=5, relief="ridge", command=sign_up)
        sign_up_btn.pack(pady=20)

        # login function

        def login_func():
            win.destroy()
            login_page.Login()
            

        # login label

        login_lbl = Button(head_frame, text="Already have an account?", fg="blue", cursor="hand2",
        command=login_func, bd=0)
        login_lbl.pack()


        # time & date
        def time_func():
            global time, time_date
            time = datetime.datetime.now()
            time_date = time.strftime("%H:%M:%S %p\n%Y/%m/%d")

            time_lbl.config(text=time_date)
            time_lbl.after(1000, time_func)


        time = datetime.datetime.now()
        time_date = time.strftime("%H:%M:%S %p\n%Y/%m/%d")


        time_lbl = Label(win, text=time_date, font=("courier", 15))
        time_lbl.pack(pady=20)
        time_func()
        win.mainloop()

if __name__ == "__main__":
    run_main_page = Main_Page()

