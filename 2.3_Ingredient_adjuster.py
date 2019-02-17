"""
A cookie recipe calls for the following ingredients:

    1.5 cups of sugar
    1 cup of butter
    2.75 cups of flour

    The recipe produces 48 cookies with this amount of ingredients.
    Write a program that asks the user how many cookies they want to
    make, and then displays the number of cups (to two decimal places)
    of each ingredient needed for the specified number of cookies.
"""
"""
Here, I divided each ingredient by 48 so that the program registers the amount of ingredients for one cookie.
"""
sugar = 1.5/48
butter = 1/48
flour = 2.75/48

cookies = int(input("How many cookies would you like to make? "))

"""
Mathematics for total ingredients.
"""
sugar_required = sugar * cookies
butter_required = butter * cookies
flour_required = flour * cookies

print("To make " + str(cookies) + " cookies")
print("you need " + str(sugar_required) + " cups of sugar.")
print("You need " + str(butter_required) + " cups of butter.")
print("You need " + str(flour_required) + " cups of flour.")

"""
Here is the required amount of ingredients needed to make 100 cookies.
"""
