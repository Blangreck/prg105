days_worked = int(input("Please enter how many days you worked: "))
total_number_of_pennies = 0

print("Day\tSalary")
for current_day in range(1, days_worked + 1):
    pennies_for_the_day = 2 ** current_day
    total_number_of_pennies += pennies_for_the_day
    print(current_day + 1, "\t", pennies_for_the_day)

total_pay = total_number_of_pennies * 0.01

print("\nTotal pay: $", total_pay)
