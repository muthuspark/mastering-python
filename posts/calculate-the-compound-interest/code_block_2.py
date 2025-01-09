import math

def calculate_continuous_compound_interest(principal, rate, time):
  """Calculates compound interest with continuous compounding."""
  amount = principal * math.exp(rate * time)
  return amount

principal = 1000
rate = 0.05
time = 5

future_value_continuous = calculate_continuous_compound_interest(principal, rate, time)
print(f"Future value (continuous compounding): ${future_value_continuous:.2f}")