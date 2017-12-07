import smtplib

# For Gmail host = 'smtp.gmail.com', port = 587
# For Yahoo host = 'smtp.mail.yahoo.com', port = 465 or port = 587
# For Outlook host = 'smtp-mail.outlook.com', port = 587

host = 'HOST'
port = PORT

user = "SENDER'S USERNAME"
password = "SENDER'S PASSWORD"
receiver = "RECEIVER'S EMAIL ADDRESS"

message = """From: SENDER'S NAME <SENDER'S EMAIL ADDRESS>
To: RECEIVER'S NAME <RECEIVER'S EMAIL ADDRESS>
Subject: Demo Email Test from python script

This is a test e-mail body.
"""

#create smtp object for connection with the server
#connect to gmail's SMTP server with the port provided by google
conn = smtplib.SMTP(host, port)

#identify yourself to ESMPT server
conn.ehlo()

#For Security purpose
conn.starttls()
conn.ehlo()

#Login to the server
conn.login(user, password)
#print(conn.verify(receiver))

#Send Message
conn.sendmail(user, receiver, message)

#Close or Terminate the connection from the server
conn.quit()