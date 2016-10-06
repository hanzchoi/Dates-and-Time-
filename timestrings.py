"""Create a function named to_string that takes a datetime and gives
        back a string in the format "24 September 2012".
"""

# Examples
# to_string(datetime_object) => "24 September 2012"
# from_string("09/24/12 18:30", "%m/%d/%y %H:%M") => datetime
import datetime


def to_string(datetime_object):
    return datetime_object.strftime("%d %B %Y")


# Create a new function named from_string that takes two arguments:
# a date as a string and an strftime-compatible format string,
# and returns a datetime created from them.

def from_string(arg1, arg2):
    return datetime.datetime.strptime(arg1, arg2)
