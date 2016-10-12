import datetime
import pytz

"""
pacific = datetime.timezone(datetime.timedelta(hours=-8))

eastern = datetime.timezone(datetime.timedelta(hours=-5))

naive = datetime.datetime(2014, 4, 21, 9)

aware = datetime.datetime(2014, 4, 21, 9, tzinfo=pacific)

aware.astimezone(eastern)

auckland = datetime.timezone(datetime.timedelta(hours=13))

mumbai = datetime.timezone(datetime.timedelta(hours=5, minutes=30))

"""

pacific = pytz.timezone('US/Pacific')

eastern = pytz.timezone('US/Eastern')

fmt = '%Y-%m-%d %H:%M:%S %Z%z'

utc = pytz.utc

start = pacific.localize(datetime.datetime(2014, 4, 21, 9))

start.strftime(fmt)

start_eastern = eastern.astimezone(eastern)

start_utc = datetime.datetime(2014, 4, 21, 1, tzinfo=utc)

start_utc.strtime(fmt)

start_pacific = start_utc.astimezone(pacific)

auckland = pytz.timezone('Pacific/Auckland')

mumbai = pytz.timezone('Asia/Calcutta')

apollo_13_naive = datetime.datetime(1970, 4, 11, 14, 13)

apollo_13_eastern = eastern.localize(apollo_13_naive)

apollo_13_utc = apollo_13_eastern.astimezone(utc)

apollo_13_utc.astimezone(pacific).strftime(fmt)

apollo_13_utc.astimezone(auckland).strftime(fmt)

