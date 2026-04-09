#Tyler Nguyen

name = input("Enter name: ")
if len(name) == 0 or name.isspace():
    name_msg = "Name cannot be blank"
elif len(name) < 3:
    name_msg = "Name too short"
elif not name.isalpha():
    name_msg = "Name must be alphabetic"
else:
    name_msg = "valid"

account = input("Enter account number: ")
if len(account) == 0 or account.isspace():
    account_msg = "Account number cannot be blank"
elif not account.isdigit():
    account_msg = "Account number must be numeric"
elif len(account) != 9:
    account_msg = "Account number must be 9 digits"
else:
    account_msg = "Valid"

payment = input("Enter payment amount: ")
if len(payment) == 0 or payment.isspace():
    payment_msg = "Payment cannot be blank"
else:
    amount = float(payment)
    if amount < 0:
        payment_msg = "Payment cannot be negative"
    elif amount == 0:
        payment_msg = "Payment cannot be zero"
    else:
        payment_msg = "valid"

print()
print("Name:", name, name_msg)
print("Account Number:", account, account_msg)
print("Payment:", payment, payment_msg)
