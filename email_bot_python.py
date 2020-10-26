# -*- coding: utf-8 -*-
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time

## Define properties for sending email
email_from = 'bergamimg@usp.br'
password = open(r'C:\Users\GitHub\6.SMTP\password.txt').read().strip()

recipients = ['bergamim_guilherme@outlook.com', 'bergamimg@usp.br']
email_to = recipients

## Create message content
msg = MIMEMultipart('Send_Email')
msg['Subject'] = "Daily Weather Forecast"
msg['From'] = email_from
msg['To'] = ", ".join(recipients)

text = ''' Hello. \nYou're receiving a mail from a test bot!\nBy the way, 
           check this picture: https://i.pinimg.com/736x/b8/09/27/b80927e5d832e5535c1b3fbf5be51689.jpg
       '''

html = '''\
<html>
 <head></head>
 <body>
  <p>Hello.<br>
    You're receiving a mail from a test bot!\nBy the way, 
    check this picture: <a href= "https://i.pinimg.com/736x/b8/09/27/b80927e5d832e5535c1b3fbf5be51689.jpg">link</a>.
  </p> 
 </body> 
</html>
      '''

## Record the MIME types for both parts - text/plain and text/html
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

## Attach parts into message
msg.attach(part1)
msg.attach(part2)

## Send the message using SMTP server
server = smtplib.SMTP('smtp.gmail.com', 587, timeout=360)
server.ehlo()
server.starttls()
server.login(email_from, password)

## Loop to send it more than once
for i in range(3):
        server.sendmail(email_from, recipients, msg.as_string())
server.quit()
