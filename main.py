from tkinter import *
import random
import webbrowser
import datetime
import re
from tkinter import messagebox

# app setting

win = Tk()
win.title("login")
win.geometry("500x500")
win.resizable(False, False)
app_icon = PhotoImage(file="app-icon.jpg")
win.iconphoto(False, app_icon)

# head frame

head_frame = Frame(win)
head_frame.pack()

# email & password

entry_lbl = Label(head_frame, text="Fill the blanks to login", font=("courier", 15))
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
    global captcha, captcha_text
    captcha_text = str(random.randint(10000, 99999))
    captcha = ""
    for item in captcha_text:
        captcha += "  "
        captcha += item


captcha_func()


def change_captcha():
    captcha_func()
    captcha_lbl.config(text=captcha)


captcha_lbl = Button(head_frame, text=captcha, font=("courier, 12"), cursor="hand2", bd=0,
                     command=change_captcha)
captcha_lbl.pack(pady=15)

captcha_entry = Entry(head_frame)
captcha_entry.pack()

# password validation
password_regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$"
match_re = re.compile(password_regex)

def pass_validation():
    global captcha
    if re.search(match_re, password_input.get()):
        if password_input.get() == password_confirm_input.get():
            if captcha_entry.get() == captcha:
                messagebox.showinfo("Logged in", "You successfully logged in!")
            else:
                messagebox.showerror("captcha error", "Please fill the captcha blank to submit that you are not a bot!!")
        else:
            messagebox.showerror("password confirmation error", "Password doesn't match!!")
    else:
        messagebox.showerror("password error", "Invalid password!!")

# login button func


def login():
    email = email_input.get()
    if check(email) == False:
        messagebox.showerror("email error", "wrong email!! try again")
    else:
        pass_validation()


# login button

login_btn = Button(head_frame, text="login", width=20, bd=5, relief="ridge", command=login)
login_btn.pack(pady=20)

# forget password

forget_password = Label(head_frame, text="Forgot password?", fg="blue", cursor="hand2")
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
time_lbl.pack(pady=30)

date_lbl = Label(win, text=time_now, font=("courier", 15), borderwidth=2, relief="solid")
date_lbl.pack(pady=0)

time_func()

win.mainloop()

