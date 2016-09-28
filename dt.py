import datetime

now = datetime.datetime.now()

two = now.replace(hour=14)

two = two.replace(minute=30)

datetime.timedelta(hours=5)

now + datetime.timedelta(days=3)

now + datetime.timedelta(days=-5)

# OR this works as well

now - datetime.timedelta(days=5)

now.date()

now.time()

hour = datetime.timedelta(hours=1)

workday = hour * 9

tomorrow = datetime.datetime.now().replace(hour=9, minute=0) + datetime.timedelta(days=1)

appointment = datetime.timedelta(minutes=45)

start = datetime.datetime(2014, 11, 1, 12, 45)

end = start + appointment

today = datetime.datetime.combine(datetime.date.today(), datetime.time())

now.timestamp() #  POSIX time stamp
