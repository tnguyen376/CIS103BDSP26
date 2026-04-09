#Tyler Nguyen

roman_dict = {
    1:"I", 2:"II", 3:"III", 4:"IV", 5:"V", 6:"VI",
    7:"VII", 8:"VIII", 9:"IX", 10:"X", 11:"XI", 12:"XII",
    13:"XIII", 14:"XIV", 15:"XV", 16:"XVI", 17:"XVII", 18:"XVIII",
    19:"XIX", 20:"XX", 21:"XXI", 22:"XXII", 23:"XXIII", 24:"XXIV"
}

print("Dictionary:", roman_dict)

again = "y"

while again == "y":

    number = 1

    while number > 0:

        try:
            user_input = input("Enter a number: ")

            if user_input == "":
                print("Input cannot be blank")
                continue

            number = int(user_input)

        except:
            print("Input must be an integer")
            continue

        if number <= 0:
            break

        if number in roman_dict:
            print("Roman numeral:", roman_dict[number])

        if number not in roman_dict:

            add = input("Number not found. Add it? (y/n): ")

            if add == "y":

                roman = input("Enter Roman numeral: ").upper()

                valid = True
                for letter in roman:
                    if letter not in "IVXLCDM":
                        valid = False

                if valid:
                    roman_dict[number] = roman
                    print("Added:", number, "=", roman)
                else:
                    print("Roman numeral must contain only IVXLCDM")

    print("Current dictionary:", roman_dict)

    again = input("Run program again? (y/n): ")
