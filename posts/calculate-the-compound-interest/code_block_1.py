principal = 1000
rate = 0.05
time = 5

future_value_annual = calculate_compound_interest(principal, rate, time, 1)
print(f"Future value (annual compounding): ${future_value_annual:.2f}")

future_value_semi_annual = calculate_compound_interest(principal, rate, time, 2)
print(f"Future value (semi-annual compounding): ${future_value_semi_annual:.2f}")

future_value_quarterly = calculate_compound_interest(principal, rate, time, 4)
print(f"Future value (quarterly compounding): ${future_value_quarterly:.2f}")

future_value_monthly = calculate_compound_interest(principal, rate, time, 12)
print(f"Future value (monthly compounding): ${future_value_monthly:.2f}")
