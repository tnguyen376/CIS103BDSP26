#Tyler Nguyen
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

rain = []

for m in months:
    value = float(input("Enter rainfall for " + m + ": "))
    
    if value < 0:
        print("Rainfall cannot be negative.")
        value = float(input("Enter rainfall for " + m + " again: "))
        
    rain.append(value)

print("Data list:", rain)

highest = max(rain)
lowest = min(rain)
total = sum(rain)
average = total / len(rain)

high_month = months[rain.index(highest)]
low_month = months[rain.index(lowest)]

print("Highest:", high_month, highest)
print("Lowest:", low_month, lowest)
print("Total:", total)
print("Average:", average)
