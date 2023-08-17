import smtplib
from email.message import EmailMessage

email_content = """
Hello,
This is a test email.

Thanks"""

email = EmailMessage()
email['subject'] = "Test Email"
email["from"] = "Mailgun Sandbox <postmaster@sandbox2d25cad9da7148c88a9789b31a2b96ee.mailgun.org>"
email["to"] = "Soap Mactavish<soapcod12321@gmail.com>"

email.set_content(email_content)

with smtplib.SMTP(host="smtp.mailgun.org", port=587) as smtp:
    smtp.login(
        "postmaster@sandbox2d25cad9da7148c88a9789b31a2b96ee.mailgun.org", "f5d5cb0ad9d16683138741e7f248f813-ee16bf1a-91983e5c")
    smtp.send_message(email)
    print("Email sent successfully")
