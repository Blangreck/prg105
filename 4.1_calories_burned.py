calories_burned_per_minute = 4.2

for number_of_minutes in range(10, 31, 5):
    number_of_calories_burned = (number_of_minutes / 1) * calories_burned_per_minute
    print("You will burn", number_of_calories_burned, "in", number_of_minutes)
