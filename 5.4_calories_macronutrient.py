fat_calories = 9
carbs_calories = 4
protein_calories = 4


def main():
    fat = fats()
    carb = carbs()
    protein = proteins()
    calculate_calories(fat, carb, protein)


def fats():
    fat = float(input("How many grams of fat did you eat today?: "))
    fat_total = fat * fat_calories
    print("Your total calories of fat for the day were: ", (fat_total))
    return fat_total


def carbs():
    carbs = float(input("How many grams of carbs did you eat today?: "))
    carbs_total = carbs * carbs_calories
    print("Your total calories of carbs for the day were: ", (carbs_total))
    return carbs_total


def proteins():
    protein = float(input("How many grams of protein did you eat today?: "))
    protein_total = protein * protein_calories
    print("Your total calories of protein for the day were: ", (protein_total))
    return protein_total


def calculate_calories(fat_grams, carb_grams, protein_grams):
    total_calories = (fat_grams + carb_grams + protein_grams)
    print("Your total calories consumed for the day were: ", (total_calories))


main()
