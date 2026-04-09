# Tyler Nguyen
discount_rate = 0
price_per_pound = 0.99
pounds = float(input("Enter number of pounds to purchase: "))
if pounds <= 0:
    print("Error: pounds must be greater than zero.")
else:
    if pounds < 10:
        discount_rate = 0
    elif pounds < 100:
        discount_rate = 0.10
    elif pounds < 1000:
        discount_rate = 0.20
    elif pounds < 10000:
        discount_rate = 0.30
    else:
        discount_rate = 0.40
    
gross_sales = pounds * price_per_pound
discount_amount = gross_sales * discount_rate
final_amount = gross_sales - discount_amount
    
print("Number of pounds", pounds)
print("Gross sales", format(gross_sales, ".2f"))
print("Discount:", format(discount_amount, ".2f"))
print("Final Amount:", format(final_amount, ".2f"))
