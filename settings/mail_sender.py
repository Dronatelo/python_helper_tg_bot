import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders

from random import randint

#create passowrd
def get_value():
    value = randint(100000000,999999999)
    return value

mails = ["*****"]   

def send_mail_password(mail):
    try:
        #get password
        password = get_value()
        #connect to server mail
        sender = "****"
        password_mail = "****"

        #settings for mail
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(sender,password_mail)
        
        if mail in mails:
            server.sendmail(sender,mail,f"Subject: PASSWORD\n{password}")
            return password
        else:
            return "Ваша почта не в списке!"
    except Exception as ex:
        return f"{ex}\n check login or password!"

