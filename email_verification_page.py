
from tkinter import *
import email_verfication_send as evs
from main_page import email_input


class Email_Page:
        minute = 1
        second = 60
        timer = f"0{minute}:{second}"

        
        def __init__(self):
                root = Tk()
                root.title("Email validation code")
                root.geometry("500x200")
                root.resizable(False, False)
                app_icon = PhotoImage(file="app-icon.jpg")
                root.iconphoto(False, app_icon)

                # code
                code_lbl = Label(root,text="""We will send a validation code to your email.
click to send""", font=("Courier",10))
                code_lbl.pack()

                def send_func():
                        evs.Send_Email.user_email = email_input.get()
                        import email_verfication_send
                        global timer_lbl
                        validation_code_btn.destroy()
                        code_lbl.config(text="Enter the code")
                        code_entry = Entry(root)
                        code_entry.pack(pady=10)
                        submit_btn = Button(root, width=10, text="Submit", font="courier", bd=5, relief="ridge")
                        submit_btn.pack(pady=5)


                validation_code_btn = Button(root,text="send", width=6, font=("courier", 12), bd=5, relief="ridge",command=send_func)
                validation_code_btn.pack()


                def timer_func():
                        Email_Page.second -= 1
                        if Email_Page.second == 0:
                                Email_Page.second == 60
                                Email_Page.minute -= 1
                        # timer_lbl.config(text=Email_Page.timer)

                timer_func()


                root.mainloop()

Email_Page()