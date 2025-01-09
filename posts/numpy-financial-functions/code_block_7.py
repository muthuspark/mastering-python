rate = 0.06 / 12 # Monthly interest rate
nper = 5 * 12     # Total number of payments
pv = 20000        # Loan amount
pmt = npf.pmt(rate, nper, pv)
print(f"Monthly Payment: {pmt:.2f}")
