# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
overperiod = 30
payment = 2684.11
total_paid = 0.0
interest = 0.0
month = 1
extraPaid = 1000
forMonths = 12
while principal > 0:
    if forMonths > 1:
        principal = principal - extraPaid
        forMonths -=1     
    principal = principal * (1 +rate/12 ) - payment
    total_paid = total_paid + payment
    print ('month - principal', month, principal)    
    month +=1
   
#print('total paid', total_paid)    
# using f-string for printing
print(f'total paid {total_paid:0.2f}')
