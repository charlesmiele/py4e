# Turning ex_03_01 into a function

def computepay(hours, rate):
    if hours > 40:
        regular_pay = 40*rate
        overtime_pay = (hours-40) * (rate * 1.5)
        pay = regular_pay + overtime_pay
    else:
        pay = hours*rate
    return pay


hours = input('Enter Hours: ')
rate = input('Enter Rate: ')
float_hours = float(hours)
float_rate = float(rate)


pay = computepay(float_hours, float_rate)
print('Pay', pay)
