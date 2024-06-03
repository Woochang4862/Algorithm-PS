import sys
from datetime import datetime, timedelta
A,B=map(int,sys.stdin.readline().split())
C=int(sys.stdin.readline())
now = datetime.now()
now = now.replace(hour=A)
now = now.replace(minute=B)
now += timedelta(minutes=C)
print(now.hour, now.minute)