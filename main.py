from email.mime import image
from msilib.schema import File
from pydoc import cli
from tkinter import *
import random
import webbrowser
import datetime
import re
from tkinter import messagebox
import captcha
from captcha.image import ImageCaptcha
from PIL import ImageTk, Image
import click


# app setting

win = Tk()
win.title("Sign up")
win.geometry("500x500")
win.resizable(False, False)
app_icon = PhotoImage(file="app-icon.jpg")
win.iconphoto(False, app_icon)


# head frame

head_frame = Frame(win)
head_frame.pack()

# email & password

entry_lbl = Label(head_frame, text="Fill the blanks to sign up", font=("courier", 15))
entry_lbl.pack(pady=20)

email_input_lbl = Label(head_frame, text="Email", font=("courier, 10"))
email_input_lbl.pack()
email_input = Entry(head_frame, width=50)
email_input.pack()

password_input_lbl = Label(head_frame, text="Password", font=("courier, 10"))
password_input_lbl.pack()

password_confirm_input = Entry(head_frame, width=50, show="*")
password_confirm_input.pack()

password_confirm_input_lbl = Label(head_frame, text="Confirm Password", font=("courier, 10"))
password_confirm_input_lbl.pack()

password_input = Entry(head_frame, width=50, show="*")
password_input.pack()

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
recaptcha_btn.place(x=240, y=215)


# password validation
password_regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$"
match_re = re.compile(password_regex)

def pass_validation():
    global captcha
    if re.search(match_re, password_input.get()):
        if password_input.get() == password_confirm_input.get():
            if captcha_entry.get() == captcha_text:
                messagebox.showinfo("Logged in", "You successfully logged in!")
            else:
                messagebox.showerror("captcha error", "Please fill the captcha blank to submit that you are not a bot!!")
        else:
            messagebox.showerror("password confirmation error", "Password doesn't match!!")
    else:
        messagebox.showerror("password error", "Invalid password!!")

# sign_up button func


def sign_up():
    email = email_input.get()
    if check(email) == False:
        messagebox.showerror("email error", "wrong email!! try again")
    else:
        pass_validation()


# sign up button

sign_up_btn = Button(head_frame, text="sign up", width=20, bd=5, relief="ridge", command=sign_up)
sign_up_btn.pack(pady=20)

# forget password

forget_password = Label(head_frame, text="Already have an account?", fg="blue", cursor="hand2")
forget_password.pack()


def callback(url):
    webbrowser.open_new_tab(url)


forget_password.bind("<Button-1>", lambda e:callback("http://www.google.com"))

# time & date


def time_func():
    global time, time_date, time_now
    time = datetime.datetime.now()
    time_date = time.strftime("%Y/%m/%d")
    time_now = time.strftime("%H:%M:%S")
    time_lbl.config(text=time_now)
    time_lbl.after(1000, time_func)
    date_lbl.config(text=time_date)


time = datetime.datetime.now()
time_date = time.strftime("%Y/%m/%d")
time_now = time.strftime("%H:%M:%S")

time_lbl = Label(win, text=time_date, font=("courier", 15), borderwidth=2, relief="solid")
time_lbl.pack(pady=20)

date_lbl = Label(win, text=time_now, font=("courier", 15), borderwidth=2, relief="solid")
date_lbl.pack(pady=0)

time_func()

win.mainloop()

