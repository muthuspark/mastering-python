def calculate_simple_interest(principal, rate, time):
  """
  Calculates simple interest.

  Args:
    principal: The principal amount.
    rate: The annual interest rate (as a percentage).
    time: The time period in years.

  Returns:
    The simple interest.  Returns an error message if input is invalid.
  """
  try:
    if principal < 0 or rate < 0 or time < 0:
      return "Error: Principal, rate, and time must be non-negative values."
    simple_interest = (principal * rate * time) / 100
    return simple_interest
  except TypeError:
      return "Error: Invalid input type. Please use numbers."


principal = 1000
rate = 5
time = 2
interest = calculate_simple_interest(principal, rate, time)

if isinstance(interest, str): #check for error message
    print(interest)
else:
    print(f"The simple interest is: {interest}")


principal = 1000
rate = 5.5
time = 2.5
interest = calculate_simple_interest(principal, rate, time)

if isinstance(interest, str): #check for error message
    print(interest)
else:
    print(f"The simple interest is: {interest}")

principal = -1000 #test with negative value
rate = 5
time = 2
interest = calculate_simple_interest(principal, rate, time)

if isinstance(interest, str): #check for error message
    print(interest)
else:
    print(f"The simple interest is: {interest}")

principal = "abc" #test with string
rate = 5
time = 2
interest = calculate_simple_interest(principal, rate, time)

if isinstance(interest, str): #check for error message
    print(interest)
else:
    print(f"The simple interest is: {interest}")