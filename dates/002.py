"""
Date formatting."""

from datetime import datetime

now = datetime.now()
print(now)

# use strftime to format the datetime.
now_latam = now.strftime('%d/%m/%Y')
print(now_latam)