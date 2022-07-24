from tkinter import *

class Email_Page:
    def __init__(self):
        root = Tk()
        root.title("Email validation code")
        root.geometry("500x200")
        root.resizable(False, False)
        app_icon = PhotoImage(file="app-icon.jpg")
        root.iconphoto(False, app_icon)

        # code
        code_lbl = Label(root,text="""Enter the validation code """, font=("Courier",10))
        code_lbl.pack()
        code_entry = Entry(root)
        code_entry.pack()


        code_Validity_time_lbl = Label(root, text="code Validity time : ", font=("courier", 10))
        code_Validity_time_lbl.pack()

        submit_btn = Button(root, width=10, text="Submit", font="courier", bd=5, relief="ridge")
        submit_btn.pack()

        root.mainloop()


Email_Page()