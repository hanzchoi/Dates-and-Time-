import datetime

"""
    Write a function named minutes that takes two datetimes and, using timedelta.total_seconds() to get the number of
     seconds,
    returns the number of minutes, rounded, between them.
     The first will always be older and the second newer. You'll need to subtract the first from the second.
"""

def minutes(dt1, dt2):
  return round((dt2.timestamp() - dt1.timestamp()) / 60)