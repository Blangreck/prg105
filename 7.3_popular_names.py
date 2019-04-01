"""
write a program that reads the contents of the two files into two separate lists. The user should be able to enter
a boy's name or a girl's name. The application should check both lists, and then display messages indicating whether
the names were among the most popular if the name was on one of the lists or that the name was not on the lists of
popular names.
"""


def main():
    girls = []
    boys = []
    girl_in = open("GirlNames.txt", "r")
    boy_in = open("BoyNames.txt", "r")

    for girl in girl_in:
        the_girl = girl.strip("\n")
        girls.append(the_girl)

    for boy in boy_in:
        the_boy = boy.strip("\n")
        boys.append(the_boy)

    girl_in.close()
    boy_in.close()

    test = input("Please enter a name: ")

    if test in girls:
        print(test + " is one of the most popular names for a girl")
    elif test in boys:
        print(test + " is one of the most popular names for a boy")
    else:
        print(test + " is not a popular name. ")

main()

