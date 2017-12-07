import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#MIME = Multipurpose Internet Mail Extensions


def send_html_email(receiver, user, password, subject, body):
    '''With this function we can send html email.'''

    # For Gmail host = 'smtp.gmail.com', port = 587
    # For Yahoo host = 'smtp.mail.yahoo.com', port = 465 or port = 587
    # For Outlook host = 'smtp-mail.outlook.com', port = 587

    host = 'HOST'
    port = PORT

    message = MIMEMultipart()
    message['To'] = receiver
    message['From'] = user
    message['subject'] = subject
    #message.preamble = 'Shubham Jante'

    html_body = MIMEText(body, 'html')
    message.attach(html_body)

    conn = smtplib.SMTP(host, port)
    conn.ehlo()
    conn.starttls()
    conn.ehlo()
    conn.login(user, password)
    conn.sendmail(user, receiver, message.as_string())
    conn.quit()


user = "SENDER'S USERNAME"
password = "SENDER'S PASSWORD"
receiver = "RECEIVER'S EMAIL ADDRESS"
subject = 'HTML Body'

body = ""
filename = 'billing.html'
file = open(filename, 'r')

for line in file:
    body += line
file.close()

send_html_email(receiver, user, password, subject, body)
