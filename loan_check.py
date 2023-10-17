loan_size = int(input('Loan size: '))
credit = int(input('Credit: '))
income = int(input('Income: '))
down_payment = int(input('Down payment: '))

is_qualified = False

if loan_size >= 5: 
    if credit >= 7 and income >= 7:
       is_qualified = True
    elif credit >= 7 or income >= 7:
        if down_payment >= 5:
            is_qualified = True
        else:
            is_qualified = False
    else:
        is_qualified = False

else:
    if credit < 4:
        is_qualified = False
    else:
        if income >= 7 or down_payment >= 7:
            is_qualified = True 
        elif income >= 4 and down_payment >= 4:
            is_qualified = True
        else:
            is_qualified = False
            
if is_qualified:
    print('The decision is yes. You are qualified for a loan.')
else:
    print('The decision is no. You do not qualify for a loan.')
        
   
       
    
