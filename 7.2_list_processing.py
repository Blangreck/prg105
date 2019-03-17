"""1. Have a function that creates a list of 20 random integers between 1 and 100 (Assign them dynamically,
    store the list in a variable.)

2. Have a function get a number from the user that is between 1 and 100 (validate to ensure a number between
    1 and 100 was entered instead of text or something out of range using a try and except statement).

3. Pass both the list and the user's number to a function and have it display all numbers in the list that is
    greater than the user's number. If there are not any, display a message that explains there are no numbers in
    the list greater than the entered number."""


def list_numbers():
    index = 0
    import random
    number_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    while index < 20:
        number_list[index] = (random.randint(0, 100))
        index = index + 1
    return number_list


def user_value():
    user_input = float(input('Select a number please: '))
    if user_input < 1 or user_input > 100:
        print('Sorry, that is not a valid entry')
        user_number = float(input('Select a number please: '))
    return user_input


def higher_number(user_number, number_list):
    index = 0
    if number_list[index] > user_number:
        print(number_list)
        index += 1

    else:
        print('There is no number higher than the number you entered. ')


def main():
    index = 0
    user_input = user_value()
    number_list = list_numbers()
    print(number_list)
    while index < 20:
        if number_list[index] > user_input:
            print('This number is on your list and is higher that your input: ', number_list[index])
        index = index + 1


main()
