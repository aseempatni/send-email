
import smtplib
from email.mime.text import MIMEText

def send_email(message,subject,toaddrs):

    fromaddr = 'Here, enter your gmail address'
    username = 'enter your gmail username'
    password = 'enter your gmail password'
    
    
    msg = MIMEText(message, 'html')
    
    msg['Subject']  = subject
    
    msg['From']=fromaddr
    
    msg['Reply-to'] = 'no-reply'
    
    msg['To'] = toaddrs
    
    server = smtplib.SMTP('smtp.gmail.com:587')
    
    server.starttls()
    
    server.login(username,password)
    
    server.sendmail(fromaddr, [toaddrs], msg.as_string())
    server.quit()
   


subject = raw_input("Enter your subject?\n")
message = raw_input("Enter your mesage?\n")
toaddrs = raw_input("Enter receiver email address?\n")
counter = raw_input("How many emails you want to send?\n")
for i in range(int(counter)):
    send_email(str(message),str(subject),str(toaddrs))