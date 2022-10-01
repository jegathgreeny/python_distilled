principle = 1000  # inital amount
rate = 0.05  # interest rate
period = 5  # time period

year = 1

while year <= period:
    principle *= 1 + rate
    # '0.2f' a floating-point number with two decimal places of accuracy.
    print(f'{year} {principle:0.2f}')
    year += 1
