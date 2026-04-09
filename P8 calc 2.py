# Tyler Nguyen
def acres_to_hectares(a):
    return a * 0.4047

def quarts_to_liters(q):
    return q * 0.946353

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5 / 9 + 273.15

again = 'y'
while again == 'y':
    try:
        a = float(input('Enter acres: '))
        if a <= 0:
            raise ValueError
        print(a, 'converts to', acres_to_hectares(a), 'hectares')
    except:
        print('Input error - acres')
    try:
        q = float(input('Enter quarts: '))
        if q <= 0:
            raise ValueError
        print(q, 'converts to', quarts_to_liters(q), 'liters')
    except:
        print('Input error - quarts')
    try:
        f = float(input('Enter fahrenheit: '))
        if f <= 0:
            raise ValueError
        print(f, 'converts to', fahrenheit_to_kelvin(f), 'kelvin')
    except:
        print('Input error - fahrenheit')
    again = input('again y/n? ').lower()
print('--done')
