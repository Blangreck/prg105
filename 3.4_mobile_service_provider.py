""" Package A:	For $39.99 per month 450 minutes are provided. Additional minutes are $0.45 per minute.
    Package B:	For $59.99 per month 900 minutes are provided. Additional minutes are $0.40 per minute.
    Package C:	For $69.99 per month unlimited minutes provided."""

package = str(input("Which package did you choose, a, b, or c?"))

if package == "a" or package == "A":
    minutes = int(input("How many minutes have you used this month?"))
    if minutes > 450:
        total = 39.99 + (minutes - 450) * .45
        print("You owe $" + format(total, ",.2f"))

    else:
        print("You owe $39.99")

elif package == "b" or package == "B":
    minutes = int(input("How many minutes have you used this month?"))
    if minutes > 900:
        total = 59.99 + (minutes - 900) * .40
        print("You owe $" + format(total, ",.2f"))

    else:
        print("You owe $59.99")

elif package == "c" or package == "C":
    print("You owe $79.99")
