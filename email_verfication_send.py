import smtplib
from email.message import EmailMessage
import random 



class Send_Email:
    user_email = "pasha.adel2@gmail.com"
    host_email = "smtp.gmail.com"
    host_email_user = "amiradelpour0901@gmail.com"
    host_email_password = "hnhzbipxfctpfwhh"
    email_port_ssl = 465
    choice = random.randint(100000,999999)




    def __init__(self):
        msg = EmailMessage()
        msg["Subject"] = "Verification Code"
        msg["From"] = Send_Email.host_email_user
        msg["To"] = Send_Email.user_email
        msg.set_content(Send_Email.choice)

        with smtplib.SMTP_SSL(Send_Email.host_email, Send_Email.email_port_ssl) as server:
            server.login(Send_Email.host_email_user, Send_Email.host_email_password)
            server.send_message(msg)

Send_Email()