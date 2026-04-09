#Tyler Nguyen
import random

def powerball():
    numbers = random.sample(range(1, 70), 5)
    numbers.sort()
    print("Power Ball", format_numbers(numbers))


def mega_million():
    numbers = random.sample(range(1, 71), 5)
    numbers.sort()
    print("Mega Million", format_numbers(numbers))


def lucky_day():
    numbers = random.sample(range(1, 46), 5)
    numbers.sort()
    print("Lucky Day Lotto", format_numbers(numbers))


def lotto():
    numbers = random.sample(range(1, 53), 6)
    numbers.sort()
    print("Lotto", format_numbers(numbers))


def format_numbers(nums):
    result = ""
    for i in range(len(nums)):
        result += str(nums[i])
        if i != len(nums) - 1:
            result += ","
    return result


def menu():
    print("\n1. Powerball")
    print("2. Mega Million")
    print("3. Lucky Day lotto")
    print("4. Lotto")
    print("9. Quit")


def main():
    choice = "0"

    while choice != "9":
        menu()
        choice = input("Select option: ")

        if choice == "1":
            powerball()
            input("Hit enter key to return to menu")

        elif choice == "2":
            mega_million()
            input("Hit enter key to return to menu")

        elif choice == "3":
            lucky_day()
            input("Hit enter key to return to menu")

        elif choice == "4":
            lotto()
            input("Hit enter key to return to menu")

        elif choice == "9":
            print("Goodbye")

        else:
            print("Invalid menu selection")


main()
