import datetime

today = datetime.datetime.now()
print(today.year)
print("{:02d}".format(today.month))
print("{:02d}".format(today.day))