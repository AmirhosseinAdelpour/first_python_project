from cgi import test
from datetime import datetime
from time import time
from tkinter import *
import email_verfication_send as evs
from tkinter import messagebox
import main_page
import time

class Email_Page:
        
        def __init__(self):
                root = Tk()
                root.title("Email validation code")
                root.geometry("500x560")
                root.resizable(False, False)
                app_icon = PhotoImage(file="app-icon.jpg")
                root.iconphoto(False, app_icon)

                # head lbl
                Label(root, text="Code verification", font=("plain", 30)).pack(pady=20)

                # validation code lbl
                code_lbl = Label(root,text="""We will send a validation code to your email.
click to send""", font=("plain",15))
                code_lbl.pack()
                

                # submit func 
                def submit_func():
                        if self.minute == 0 and self.second == 0:
                                messagebox.showerror("Time out!", "Code time out! resend code")
                        elif evs.Send_Email.choice == code_entry.get():
                                messagebox.showinfo("Successfully signed in!!", "You were successfully signed in...\nEnjoy the app.. (:")
                                timer_lbl.destroy()
                        else:
                                messagebox.showerror("Invalid Code","Your code is invalid")


                # send 
                def send_func():
                        global code_entry
                        validation_code_btn.destroy()
                        code_lbl.config(text="Enter the code", font=("plain", 15 ))
                        code_entry = Entry(root)
                        code_entry.pack(pady=10)
                        submit_btn = Button(root, width=6, text="Submit", font="courier", bd=5, relief="ridge",
                        command=submit_func)
                        submit_btn.pack(pady=5)

                        # timer  lbl
                        def timer_lbl_func():
                                global timer, timer_lbl
                                self.minute = 1
                                self.second = 60
                                timer = f"0{self.minute}:{self.second}"

                                timer_lbl = Label(root, text=timer, font=("plain",12))
                                timer_lbl.pack(pady=15)
                        timer_lbl_func()

                        # resend func
                        def resend_func():
                                evs.Send_Email()
                                timer_lbl_func()
                                timer_func()
                                resend_btn.destroy()


                        # timer func

                        def timer_func():
                                global resend_btn
                                self.second -= 1
                                if self.minute == 0 and self.second == 0:
                                        resend_btn = Button(root, text="Resend Code", font=("courier", 10), fg="blue",
                                         cursor="hand2",bd=0,  command=resend_func)
                                        resend_btn.pack(pady=15)
                                        timer_lbl.destroy()

                                elif self.second == 0:
                                        self.minute -= 1
                                        self.second = 60

                                timer2 = f"0{self.minute}:{self.second}"
                                timer_lbl.config(text=timer2)
                                timer_lbl.after(1000, timer_func)
                        
                        
                        timer_func()
                
                
                # send btn 

                validation_code_btn = Button(root,text="send", width=10, font=("courier", 12), bd=5,
                 relief="ridge",command=send_func)
                validation_code_btn.pack(pady=20)

           

                root.mainloop()

if __name__ == "__main__":
        run_email_page = Email_Page()