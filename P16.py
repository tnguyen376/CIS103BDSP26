#Tyler Nguyen

def recursive_sum(n):
    if n == 0:
        return 0
    return n + recursive_sum(n - 1)

def show_addition(n):
    result = ""
    for i in range(n, 0, -1):
        result += str(i)
        if i != 1:
            result += "+"
    return result

def get_number():
    try:
        user_input = input("enter number: ")
        if user_input == "":
            print("Invalid input detected")
            return None
        num = int(user_input)
        if num < 0:
            print("Number cannot be negative")
            return None
        return num
    except:
        print("Invalid input detected")
        return None

def main():
    print("--- sum up numbers ---")
    choice = "y"
    while choice == "y":
        num = get_number()
        if num is not None:
            total = recursive_sum(num)
            addition = show_addition(num)
            print(addition + " = " + str(total))
        choice = input("Another number (y/n): ").lower()

    print("---done---")

main()
