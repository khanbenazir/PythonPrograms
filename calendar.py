import calendar

cal = calendar.TextCalendar(calendar.SUNDAY)
month = cal.formatmonth(2021, 3, 4, 0)
print(month)


# Printing Meet Days

print("Meetings for this year are as follows:")
for m in range(1, 13):
    cal1 = calendar.monthcalendar(2021, m)
    first_week = cal1[0]
    sec_week = cal1[1]
    if first_week[calendar.MONDAY] != 0:
        meetday = first_week[calendar.MONDAY]
    else:
        meetday = sec_week[calendar.FRIDAY]
    print("%10s %2d" % (calendar.month_name[m]), meetday)


# Meetings for a month

cal2 = calendar.monthcalendar(2021, 4)
print("Meetings in month of April:")
for d in range(0, 5):
    week = cal2[d]
    if week[calendar.MONDAY] != 0:
        print(calendar.month_name[4], week[calendar.MONDAY])
