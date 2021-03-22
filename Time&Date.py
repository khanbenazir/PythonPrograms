# Printing and formatting date and time and calculating duration

from datetime import date
from datetime import datetime
from datetime import timedelta

today_date = date.today()
print(today_date)
# another way of printing year month day separately
print(today_date.year, today_date.month, today_date.day)

now = datetime.now()
print("Current date & time: ", now)

# formatting date and time
print(now.strftime("Today's date: %a, %d %b, %Y"))
print(now.strftime("Current time: %I:%M:%S %p"))

# calculating the day
new = now + timedelta(weeks=2, days=6, hours=5)
print(new)
print(new.strftime("After 2 weeks 6 days 5 hours it will be %A"))

# Calculating duration
new_date = date(2021, 6, 8)
print("The date we are waiting for ", new_date)
duration = new_date - today_date
print(duration.days, "Days to go")
