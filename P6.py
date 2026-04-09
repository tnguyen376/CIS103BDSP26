#Tyler Nguyen
calories_per_minute = 4.33
again = 'y'
while again.lower() == 'y':
    print("Calorie Table Program")
    valid = "n"
    while valid == "n":
        minutes_input = input("Enter running minutes: ")
        if minutes_input == "":
            print("Minutes cannot be blank")
        elif not minutes_input.lstrip("-").isdigit():
            print("minutes must be greater than 5")
        else:
            stop_minutes = int(minutes_input)
            if stop_minutes <= 5:
                print("Minutes must be greater than 5")
            else:
                valid = "y"
    
    minutes = 5
    while minutes <= stop_minutes:
        calories = minutes * calories_per_minute
        print("minutes:", minutes, "calories:", calories)
        minutes += 5
    
    again = input("Again y/n: ")
print("-----done")
