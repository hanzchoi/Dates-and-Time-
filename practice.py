import datetime

now = datetime.datetime.now()

now.strftime('%B %d')

now.strftime('%m/%d/%y')

birthday = datetime.datetime.strptime('2017-02-22', '%Y-%m-%d')

print(birthday)

birthday_party = datetime.datetime.strptime('2017-02-22 12:00', '%Y-%m-%d %H:%M')

print(birthday_party)
