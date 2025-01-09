import pytz
from datetime import datetime

utc_now = datetime.now(pytz.utc)
print(f"UTC time: {utc_now}")

eastern = pytz.timezone('US/Eastern')
eastern_now = utc_now.astimezone(eastern)
print(f"Eastern Time: {eastern_now}")