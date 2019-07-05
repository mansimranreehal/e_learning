import random
import string
import smtplib  # import simple mail transfer protocol library
from email.mime.multipart import MIMEMultipart  # import class for using multipart
from email.mime.text import MIMEText    # import class for attached files

def generate_string(length=10):
    letter=string.ascii_letters
    pattern="".join(random.choice(letter) for i in range(length))
    return pattern

def link_send(email, link,password):
    msg = MIMEMultipart()  # assign a variable to the multipart class

    msg['From'] = 'mansimrankaur337@gmail.com'
    msg['To'] = email
    msg['Subject'] = "E_Learning"



    body = "Your password is "+password+".Your Verify link is " + str(link)
    msg.attach(MIMEText(body, "plain"))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('mansimrankaur337@gmail.com', 'reehal22simran')
    text = msg.as_string()
    server.sendmail('mansimrankaur337@gmail.com', email, text)
    server.quit()
    print("Email Sent Successfully")
