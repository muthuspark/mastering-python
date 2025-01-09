from datetime import datetime, date, time

now = datetime.now()
print(f"Current date and time: {now}")

d = date(2024, 3, 15)
print(f"Specific date: {d}")

t = time(14, 30, 0) # 2:30 PM
print(f"Specific time: {t}")

dt = datetime.combine(d, t)
print(f"Combined date and time: {dt}")