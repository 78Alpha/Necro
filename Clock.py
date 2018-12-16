import datetime, time, os
timex = 1

while timex == 1:
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute
    second = now.second
    print(str(hour) + ":" + str(minute) + ":" + str(second) + " " + str(month) + "/" + str(day) + "/" + str(year))
    time.sleep(1)