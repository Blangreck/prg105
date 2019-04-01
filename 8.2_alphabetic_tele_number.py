def main():
    num = ['-', '2', '2', '2', '3', '3', '3', '4', '4', '4', '5', '5', '5', '6', '6', '6', '7',
           '7', '7', '7', '8', '8', '8', '9', '9', '9', '9']

    output = ['-', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
           'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    phrase = input('Enter a 10 digit number in the format XXX-XXX-XXXX: ')
    num_final = ""
    for letter in phrase:
        for item in range(0, len(num)):
            if letter.upper() == num[item]:
                num_final += (output[item] + "")

    print('You typed: ', phrase)
    print('Real Number displayed as: ', num_final)


main()
