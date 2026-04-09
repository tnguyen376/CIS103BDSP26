# Tyler Nguyen
def miles_to_kilometers():
    miles = float(input("Enter miles: "))
    kilometers = miles * 1.609344
    print("Kilometers:", kilometers)
    return

def pounds_to_kilograms():
    pounds = float(input("Enter weights in pounds: "))
    kilograms = pounds * 0.45359237
    print("kilograms:", kilograms)
    return

def fahrenheit_to_celcius():
    fahrenheit = float(input("Enter temperature in fahrenheit: "))
    celcius = (fahrenheit - 32)* 5/9
    print("Celcius:", celcius)
    return

miles_to_kilometers()
pounds_to_kilograms()
fahrenheit_to_celcius()
