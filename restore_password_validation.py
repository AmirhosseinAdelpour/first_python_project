from tkinter import *
from tkinter import messagebox

class Restore_Password_Validation:

    checked = False

    def __init__(self):

        # app setting
        restore_root = Tk()
        restore_root.title("Email validation code")
        restore_root.geometry("500x560")
        restore_root.resizable(False, False)
        app_icon = PhotoImage(file="app-icon.jpg")
        restore_root.iconphoto(False, app_icon)
        restore_root.config(bg="white")

        # head lbl
        restore_head_lbl = Label(restore_root, text="Restore pasword", font=("plain", 30), bg="white")
        restore_head_lbl.pack(pady=10)

        restore_head_lbl2 = Label(restore_root, text="We will send a validation code to your email to restore your email", font=("plain", 10), bg="white")
        restore_head_lbl2.pack(pady=10)        

        # restore email & password entry
        restore_email_lbl = Label(restore_root, text="Email", font="plain", bg="white")
        restore_email_lbl.pack(pady=10)

        restore_email_input = Entry(restore_root, width=50, border=2, relief="ridge" )
        restore_email_input.pack()

        # check btn func
        def check_btn_func():
            Restore_Password_Validation.checked  = True

        # check btn

        check_btn = Checkbutton(restore_root, text="I'am not robot", cursor="hand2", command=check_btn_func, activeforeground="red", bg="white")
        check_btn.pack(pady=10)
        check_btn.flash()

        # restoe btn func
        def restore_btn_func():
            if Restore_Password_Validation.checked == True:
                messagebox.showinfo("YES", "YEAHHHH")
            else:
                messagebox.showerror("noo", "nooooo")
            
        # restore btn
        restore_btn = Button(restore_root, text="restore", font="plain", width=10, command=restore_btn_func)
        restore_btn.pack(pady=10)

        restore_root.mainloop()

if __name__ == "__main__":
    Restore_Password_Validation()