"""
Working with Timezones"""

import pytz
from datetime import datetime

now = datetime.now

mx_timezone = pytz.timezone("America/Mexico_City")
co_timezone = pytz.timezone("America/Bogota")

mx_date = now(mx_timezone)
co_date = now(co_timezone)

print('Without timezone:', now())
print('Mexico City time:', mx_date)
print('Bogota time:', co_date)