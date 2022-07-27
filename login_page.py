from tkinter import *
import random
from tkinter.font import BOLD
import captcha
from captcha.image import ImageCaptcha
from PIL import ImageTk, Image
import datetime

class Login:

    def __init__(self):
        # app setting

        login_root = Tk()
        login_root.title("Login")
        login_root.geometry("500x560")
        login_root.resizable(False, False)
        app_icon = PhotoImage(file="app-icon.jpg")
        login_root.iconphoto(False, app_icon)
        
        # login lbl
        Label(login_root, text="login", font=("plain", 30, BOLD)).pack(pady=20)

        # email & password lbl & entry

        login_email_lbl = Label(login_root, text="Email", font="courier")
        login_email_lbl.pack(pady=15)

        login_email_entry = Entry(login_root, width=50)
        login_email_entry.pack()

        login_password_lbl = Label(login_root, text="password", font="courier")
        login_password_lbl.pack(pady=15)

        login_password_entry = Entry(login_root, width=50)
        login_password_entry.pack()


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

        captcha_entry = Entry(login_root, width=20)
        captcha_entry.pack()

        # change captcha

        def change_captcha():
            captcha_func()
            captcha_lbl.config(image=my_image)

        click_image = PhotoImage(file="test.png")

        recaptcha_btn = Button(login_root, width=30,height=30, image=click_image, command=change_captcha)
        recaptcha_btn.place(x=335, y=260)

        # login btn

        login_btn = Button(login_root, text="Login", width=20, bd=5, relief="ridge")
        login_btn.pack(pady=20)

        # forgot password

        forget_password_lbl = Label(login_root, text="Forgot your password?", font=("courier"))
        forget_password_lbl.pack()

        forget_password_btn = Button(login_root, text="Click here", font=("courier", 8), fg="blue", cursor="hand2", bd=0)
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

        time_lbl = Label(login_root, text=time_date, font=("courier", 15))
        time_lbl.pack(pady=20)


        time_func()
        login_root.mainloop()
        



if __name__ == "__main__":
        Login()