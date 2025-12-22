import datetime as DateTime
time = DateTime.datetime.now()
year = time.year
month = time.month
day = time.day
if month < 10:
    month = '0' + str(month)
if day < 10:
    day = '0' + str(day)
print(year)
print(month)
print(day)