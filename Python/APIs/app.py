import requests
import time
from libs.openexchange import OpenExchangeClient

APP_ID = "8b5e4b916c9640e5bb1ad6ff86d2220b"

client = OpenExchangeClient(APP_ID)

usd_amount = 1000
from_currency = input("Enter From Currency : ")
to_currency = input("Enter From Currency : ")
start = time.time()
gbp_amount = client.convert(usd_amount, from_currency, to_currency)
end = time.time()
print(f"Time : {end-start}")
print(f'{from_currency} : {usd_amount:.2f} is {to_currency} : {gbp_amount:.2f}')
