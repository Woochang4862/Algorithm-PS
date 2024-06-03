import sys
from datetime import datetime, timedelta
h,m=map(int,sys.stdin.readline().split())
now = datetime.now()
now = now.replace(hour=h)
now = now.replace(minute=m)
now += timedelta(minutes=-45)
print(now.hour, now.minute)