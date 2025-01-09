import re

text = "My phone number is 123-456-7890 and my email is test@example.com"

phone_number = re.search(r"\d{3}-\d{3}-\d{4}", text)
if phone_number:
    print(f"Phone number: {phone_number.group(0)}")

email = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
if email:
    print(f"Email: {email.group(0)}")