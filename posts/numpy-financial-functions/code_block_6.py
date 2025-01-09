finance_rate = 0.05
reinvest_rate = 0.08
mirr = npf.mirr(values, finance_rate, reinvest_rate)
print(f"Modified Internal Rate of Return: {mirr:.2f}")