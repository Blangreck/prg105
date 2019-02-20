total_number_of_months = 0
total_inches_of_rainfall = 0
number_of_years = int(input("Please enter the number of years: "))

for current_year in range(1, number_of_years + 1):
    for current_month in range(1, 13):
        monthly_rainfall_inches = float(input("Please type the inches of rainfall for month " +
        format(current_month, "d") + ": "))
        total_inches_of_rainfall += monthly_rainfall_inches
        total_number_of_months += 1

average_rainfall = total_inches_of_rainfall / total_number_of_months

print("Number of months: " + format(total_number_of_months, "d"), "Total" + "inches of rainfall: " +
      format(total_inches_of_rainfall, ".2f"), "Average rainfall: " + format(average_rainfall, ".2f"), sep="\n")
