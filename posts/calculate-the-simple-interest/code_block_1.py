def calculate_total_amount(principal, rate, time):
    simple_interest = calculate_simple_interest(principal, rate, time)
    if isinstance(simple_interest, str):
        return simple_interest
    total_amount = principal + simple_interest
    return total_amount

principal = 1000
rate = 5
time = 2
total = calculate_total_amount(principal,rate,time)

if isinstance(total, str): #check for error message
    print(total)
else:
    print(f"The total amount is: {total}")
