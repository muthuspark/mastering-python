def calculate_compound_interest(principal, rate, time, n):
  """Calculates compound interest.

  Args:
    principal: The principal amount.
    rate: The annual interest rate (decimal).
    time: The number of years.
    n: The number of times interest is compounded per year.

  Returns:
    The future value of the investment/loan.
  """
  amount = principal * (1 + rate / n)**(n * time)
  return amount

principal = 1000  # Initial investment
rate = 0.05      # 5% annual interest rate
time = 5         # 5 years
n = 1            # Compounded annually

future_value = calculate_compound_interest(principal, rate, time, n)
print(f"Future value after {time} years: ${future_value:.2f}")