hours = input('Enter Hours: ')
rate = input('Enter Rate: ')
float_hours = float(hours)
float_rate = float(rate)
# print(float_hours, float_rate)
if float_hours > 40:
    regular_pay = 40*float_rate
    overtime_pay = (float_hours-40) * (float_rate * 1.5)
    pay = regular_pay + overtime_pay
else:
    pay = float_hours*float_rate
print('Pay:', pay)
