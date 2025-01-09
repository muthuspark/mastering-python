from datetime import datetime, timedelta

now = datetime.now()
future_date = now + timedelta(days=7, hours=3) # 7 days and 3 hours from now
print(f"Future date: {future_date}")

time_difference = future_date - now
print(f"Time difference: {time_difference}")