import datetime

"""Write a function named delorean that takes an integer. Return a datetime that is that many hours ahead from starter.
"""


starter = datetime.datetime(2015, 10, 21, 16, 29)


def delorean(int_num):
    return starter + datetime.timedelta(hours=+int_num)

print(delorean(starter))


"""Write a function named time_machine that takes an integer and a string of "minutes", "hours", "days", or "years".
 This describes a timedelta. Return a datetime that is the timedelta's duration from the starter datetime.
"""
# Remember, you can't set "years" on a timedelta!
# Consider a year to be 365 days.

## Example
# time_machine(5, "minutes") => datetime(2015, 10, 21, 16, 34)


def time_machine(int_num, time_string):
    if time_string == 'minutes':
        return starter + datetime.timedelta(minutes=int_num)
    elif time_string == 'hours':
        return starter + datetime.timedelta(hours=int_num)
    elif time_string == 'days':
        return starter + datetime.timedelta(days=int_num)
    elif time_string == 'years':
        return starter + datetime.timedelta(days=int_num * 365)

