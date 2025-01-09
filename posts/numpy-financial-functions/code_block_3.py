rate = 0.07
nper = 5
pmt = 0
fv = 2000
pv = npf.pv(rate, nper, pmt, fv)
print(f"Present Value: {pv:.2f}")