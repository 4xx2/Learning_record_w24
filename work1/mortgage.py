# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

while principal > 0:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

print('Total paid', total_paid)

# modify one

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

months = 0

while principal > 0:
    months += 1
    principal = principal * (1+rate/12) - payment
    
    if months <= 12:
        principal -= 1000
        total_paid += 1000

    total_paid = total_paid + payment

print('Total paid', round(total_paid,2))
print('months', months)

# modify two

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

months = 0

while principal > 0:
    months += 1
    if principal * (1+rate/12) > payment:
        principal = principal * (1+rate/12) - payment
    else:
        payment = principal * (1+rate/12)
        principal = 0
    
    if extra_payment_start_month <= months <= extra_payment_end_month and principal!=0:
        principal -= extra_payment
        total_paid += extra_payment

    total_paid = total_paid + payment
    print(months, round(total_paid,2), round(principal,2))

print('Total paid', round(total_paid,2))
print('Months', months)















