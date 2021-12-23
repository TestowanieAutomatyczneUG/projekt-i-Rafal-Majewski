import sys
if (len(sys.argv) != 2):
	print("Wrong number of arguments")
	sys.exit(1)

targetEmail = sys.argv[1]

data = sys.stdin.read()


import smtplib
import json
from email.message import EmailMessage

auth = json.load(open("auth.json"))["smtp"]
message = EmailMessage()
message.set_content(data)
message["Subject"] = "Testowanie Automatyczne - Projekt 1 - Wyniki testowania"
message["From"] = auth["email"]
message["To"] = targetEmail

server = smtplib.SMTP_SSL(auth["host"], auth["port"])
server.login(auth["email"], auth["password"])
print("Sending...")
server.send_message(message)
server.close()
print("Confirmation email sent from " + auth["email"] + " to " + targetEmail)
