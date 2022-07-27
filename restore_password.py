from tkinter import *
from tkinter import messagebox

class Restore_Password:

    checked = False

    def __init__(self):

        # app setting
        restore_password_root = Tk()
        restore_password_root.title("Email validation code")
        restore_password_root.geometry("500x560")
        restore_password_root.resizable(False, False)
        app_icon = PhotoImage(file="app-icon.jpg")
        restore_password_root.iconphoto(False, app_icon)

        # head lbl
        restore_password_head_lbl = Label(restore_password_root, text="Set Password", font=("plain", 30))
        restore_password_head_lbl.pack(pady=10)

        # change password validation code
        change_password_validation_code_lbl = Label(restore_password_root, text="Validation Code", font="plain")
        change_password_validation_code_lbl.pack(pady=10)

        change_password_validation_code_input = Entry(restore_password_root, width=50)
        change_password_validation_code_input.pack()
        # new password
        new_password_lbl = Label(restore_password_root, text="New Password", font="plain")
        new_password_lbl.pack(pady=10)

        new_password_input = Entry(restore_password_root, width=50)
        new_password_input.pack()

        # confirm new password
        confirm_password_lbl = Label(restore_password_root, text="Confirm Password", font="plain")
        confirm_password_lbl.pack(pady=10)

        confirm_password_input = Entry(restore_password_root, width=50)
        confirm_password_input.pack()

        # change password btn
        change_password_btn = Button(restore_password_root, text="restore", font="plain", width=10)
        change_password_btn.pack(pady=10)


        restore_password_root.mainloop()

if __name__ == "__main__":
    Restore_Password()