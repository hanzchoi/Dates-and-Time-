import datetime

pacific = datetime.timezone(datetime.timedelta(hours=-8))

eastern = datetime.timezone(datetime.timedelta(hours=-5))

naive = datetime.datetime(2014, 4, 21, 9)

aware = datetime.datetime(2014, 4, 21, 9, tzinfo=pacific)

aware.astimezone(eastern)

auckland = datetime.timezone(datetime.timedelta(hours=13))

mumbai = datetime.timezone(datetime.timedelta(hours=5, minutes=30))