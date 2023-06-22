import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Set up email credentials and server
smtp_server = 'your_smtp_server'
smtp_port = 587
username = 'your_email@example.com'
password = 'your_password'

# Create a multipart message
message = MIMEMultipart()
message['From'] = 'sender@example.com'
message['To'] = 'recipient@example.com'
message['Subject'] = 'Sample Email'

# Add body to the message
body = 'This is the body of the email.'
message.attach(MIMEText(body, 'plain'))

# Add attachment to the message
attachment_path = 'path_to_attachment_file'
attachment_name = 'attachment_file.txt'
with open(attachment_path, 'rb') as attachment:
    attachment_part = MIMEText(attachment.read(), 'plain')
    attachment_part.add_header('Content-Disposition', 'attachment', filename=attachment_name)
    message.attach(attachment_part)

# Connect to the SMTP server and send the email
try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(username, password)
        server.send_message(message)
    print('Email sent successfully!')
except Exception as e:
    print('Failed to send email:', str(e))
