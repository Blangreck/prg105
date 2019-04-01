def main():
    letters = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')

    letter = input("Enter a bunch of letters!:  ")

    highest = 0
    count = 0

    frequent_letter = ""

    for let in letters:
        for item in letter:
            if item.upper() == let:
                count += 1
        if count == highest:
            frequent_letter += let + " "
            highest = count
        elif count > highest:
            highest = count
            frequent_letter = let
        count = 0

    print("Frequnt letter: " + frequent_letter)
    print('The most frequent letter appears: ', highest, 'times')


main()
