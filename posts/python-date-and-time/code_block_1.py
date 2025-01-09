from datetime import datetime

now = datetime.now()

formatted_date_1 = now.strftime("%Y-%m-%d")  # YYYY-MM-DD
formatted_date_2 = now.strftime("%B %d, %Y") # Month DD, YYYY
formatted_time = now.strftime("%H:%M:%S")    # HH:MM:SS

print(f"Formatted date 1: {formatted_date_1}")
print(f"Formatted date 2: {formatted_date_2}")
print(f"Formatted time: {formatted_time}")