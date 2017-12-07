import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# For Gmail host = 'smtp.gmail.com', port = 587
# For Yahoo host = 'smtp.mail.yahoo.com', port = 465 or port = 587
# For Outlook host = 'smtp-mail.outlook.com', port = 587

host = 'HOST'
port = PORT

user = "SENDER'S USERNAME"
password = "SENDER'S PASSWORD"
receiver = "RECEIVER'S EMAIL ADDRESS"
subject = 'Email Subject'
body = "Please Downlod the attachment"

message = MIMEMultipart()
message['To'] = receiver
message['From'] = user
message['subject'] = subject

message.attach(MIMEText(body, 'plain'))
filename = 'Demo.pdf'
attachment = open(filename, 'rb')

file = MIMEBase('application', 'octet-stream')
file.set_payload(attachment.read())
encoders.encode_base64(file)
file.add_header('Content-Disposition', "attachment; filename= %s" % filename)

message.attach(file)

conn = smtplib.SMTP(host, port)
conn.ehlo()
conn.starttls()
conn.ehlo()
conn.login(user, password)
conn.sendmail(user, receiver, message.as_string())
conn.quit()
