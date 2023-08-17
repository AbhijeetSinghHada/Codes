import requests
mailgun_API_URL = "https://api.mailgun.net/v3/sandbox2d25cad9da7148c88a9789b31a2b96ee.mailgun.org/messages"
mailgun_API_KEY = "e527660e103cb0536c36f630f5e978a6-ee16bf1a-ab03c02d"

FROM_NAME = "Mailgun Sandbox"
FROM_EMAIL = "postmaster@sandbox2d25cad9da7148c88a9789b31a2b96ee.mailgun.org"
TO_EMAIL = "soapcod12321@gmail.com"
SUBJECT = "Hello"
CONTENT = "This is a test email from Mailgun"

request = requests.post(mailgun_API_URL, auth=("api", mailgun_API_KEY), data={
    "from": f'{FROM_NAME} <{FROM_EMAIL}>',
    'to': TO_EMAIL,
    'subject': SUBJECT,
    'text': CONTENT})
