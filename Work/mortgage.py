# mortgage.py
#
# Exercise 1.7
month = 1
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
total_payment = 0.0

while principal > 0:
    total_payment = payment + 1000 if  61 <= month <= 108 else payment
    month += 1
    principal = principal * (1+rate/12) - total_payment
    total_paid = total_paid + total_payment if principal > 0 else total_paid + total_payment + principal
print(principal, total_payment)
print('Total paid', total_paid)