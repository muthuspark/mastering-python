import datetime

now = datetime.datetime.now()
print(f"Current date and time: {now}")

specific_date = datetime.date(2024, 3, 15)
print(f"Specific date: {specific_date}")

date1 = datetime.date(2023, 1, 1)
date2 = datetime.date(2024, 1, 1)
difference = date2 - date1
print(f"Difference between dates: {difference}")