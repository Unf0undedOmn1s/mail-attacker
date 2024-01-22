import csv
from email.mime.text import MIMEText 
import re
import smtplib

fp = open("message.txt", "rb")
msg = MIMEText(fp.read().decode('utf-8'))
msg["Subject"] = "Subject Testing"
msg["From"] = "example@gmail.com"
msg["To"] = "example@gmail.com"

server = smtplib.SMTP("smtp@gmail.com", 587)
server.starttls()
server.login("sender.address@gmail.com", "sender.password")
email_data = csv.reader(open("email.csv","r"))
email_pattern= re.compile("^.+@.+\..+$")
for row in email_data:
  if (email_pattern.search(row[1])):
    del msg["To"]
    msg["To"] = row[1]
    try:
      server.sendmail("sender.address@gmail.com", row[1], msg.as_string())
    except smtplib.SMTPException:
      print ("An error has occured")
server.quit()