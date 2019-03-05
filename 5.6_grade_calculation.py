def main():
    score1 = float(input("What was your fist score? "))
    score2 = float(input("What was your second score? "))
    score3 = float(input("What was your third score? "))
    score4 = float(input("what was your fourth score? "))
    score5 = float(input("What was your fifth score? "))
    calc_average_score(score1, score2, score3, score4, score5)


def calc_average_score(score1, score2, score3, score4, score5):
    average = (score1 + score2 + score3 + score4 + score5) / 5
    print("The average score was ", (average))
    determine_grade(average)


def determine_grade(average):
    if average >= 90:
        grade = "A"
        print("The final grade is " + (grade))
    elif average >= 80:
        grade = "B"
        print("The final grade is " + (grade))
    elif average >= 70:
        grade = "C"
        print("The final grade is " + (grade))
    elif average >= 60:
        grade = "D"
        print("The final grade is " + (grade))
    else:
        print("Your grade is an F")


main()
