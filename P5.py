#Tyler Nguyen
print("Table codes: A = add, S = subtract, M = multiple, D = divide")
code = input("Select table code: ").upper()
number = float(input("Enter number for table: "))
if code == "A":
    print("Add")
    for x in range(1, 11):
        result = number + x
        print(result, "=", number, "+", x)
elif code == "S":
    print("Subtract")
    for x in range(1, 11):
        result = number - x
        print(result, "=", number, "-", x)
elif code == "M":
    print("Multiple")
    for x in range(1, 11):
        result = number * x
        print(result, "=", number, "*", x)
elif code == "D":
    print("Divide")
    for x in range(1, 11):
        result = number / x
        print(result, "=", number, "/", x)
else:
    print("Invalid table code")
print("-- done")
