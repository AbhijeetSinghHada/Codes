from datetime import datetime, time,date, timezone, timedelta

today = datetime.now()
tomorrow = today + timedelta(days=1)
datetime.now(timezone.utc)

print(today)
print(tomorrow)

print(today.strftime('%d-%m-%Y %H:%M:%S'))