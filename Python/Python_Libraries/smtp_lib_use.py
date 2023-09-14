import smtplib
from email.message import EmailMessage

email_content = """
Hello,
This is a test email.

Thanks"""

email = EmailMessage()
email['subject'] = "Test Email"
email["from"] = "Mailgun Sandbox <postmaster@sandbox2d2.mailgun.org>"
email["to"] = "Soap Mactavish<soapcod12321@gmail.com>"

email.set_content(email_content)

with smtplib.SMTP(host="smtp.mailgun.org", port=587) as smtp:
    smtp.login(
        "postmaster@sandbox2d2.mailgun.org", "API")
    smtp.send_message(email)
    print("Email sent successfully")
