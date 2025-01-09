import datetime

now = datetime.datetime.now()
print(f"Current date and time: {now}")

formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Formatted date and time: {formatted_datetime}")

date1 = datetime.date(2024, 1, 1)
date2 = datetime.date(2024, 3, 15)
difference = date2 - date1
print(f"Difference between dates: {difference.days} days")