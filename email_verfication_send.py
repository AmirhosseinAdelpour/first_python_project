import smtplib
from email.message import EmailMessage
import random
from tkinter import StringVar 



class Send_Email:
    # test, dint forget to change it
    # user_email = str()
    user_email = ""

    host_email = "smtp.gmail.com"
    host_email_user = "pasha.testcode@gmail.com"

    host_email_password = "dzijupedfyjikkli"


    email_port_ssl = 465
    choice = str(random.randint(100000, 999999))
    verification_code = ""
    for nums in  choice:
        verification_code += " "
        verification_code += nums





    def __init__(self):
        msg = EmailMessage()
        msg["Subject"] = "Verification Code"
        msg["From"] = Send_Email.host_email_user
        msg["To"] = Send_Email.user_email
        msg.set_content(Send_Email.verification_code)

        with smtplib.SMTP_SSL(Send_Email.host_email, Send_Email.email_port_ssl) as server:
            server.login(Send_Email.host_email_user, Send_Email.host_email_password)
            server.send_message(msg)


if __name__ == "__main__":
        run_send_email = Send_Email()