# mortgage.py
#
# Exercise 1.7, 1.8, 1.9, 1.10, 1.11
def input_int(msg):
    while True:
        input_user = input(msg)
        if input_user.isnumeric():
            return int(input_user)
        elif input_user == '':
            return 0
        print('Please insert whole number')

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0
extra_payment_start_month = input_int("Month start extra payment:")
extra_payment_end_month = input_int("Month end extra payment:")
extra_payment = input_int("Extra payment quantity:")

print("'Month' 'Total paid' 'Total for pay'")

while principal > 0:
    months += 1
    total_payment = payment
    if (months >= extra_payment_start_month or extra_payment_start_month == 0) and (months <= extra_payment_end_month or extra_payment_end_month == 0):
        total_payment += extra_payment
    if total_payment > principal * (1 + rate / 12):
        total_payment = principal * (1 + rate / 12)
    principal = principal * (1 + rate / 12) - total_payment
    total_paid = total_paid + total_payment
    print(f'{months:3d} {total_paid:10.2f} {principal:10.2f}')

print(f'Total paid {total_paid:0.2f}')
print(f'Months: {months}')