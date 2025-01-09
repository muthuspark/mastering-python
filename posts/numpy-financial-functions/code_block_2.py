rate = 0.05
nper = 10
pmt = 0  # No additional payments
pv = -1000 # Initial investment (negative because it's an outflow)
fv = npf.fv(rate, nper, pmt, pv)
print(f"Future Value: {fv:.2f}")