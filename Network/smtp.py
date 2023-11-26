import smtplib

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465
SMTP_USER = "kgkltd.tk@gmail.com"
SMTP_PASSWORD = "vlirsemdvqpxufwn"

server = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
server.login(SMTP_USER, SMTP_PASSWORD)

message = """From: Kalyan <kgkltd.tk@gmail.com>
Subject: Test Message

Hey there! I am Kalyan
"""

server.sendmail(from_addr=SMTP_USER,to_addrs=["srikgk333@gmail.com"], msg=message)
