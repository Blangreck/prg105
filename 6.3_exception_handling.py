def main():
    file_name = "numbers2.txt"
    total = 0
    size = 0
    average = 0

    try:
        input_file = open(file_name, "r")
        user_numbers = input_file.readline()
        user_numbers = user_numbers.rstrip('\n')

        while user_numbers != "":
            user_numbers = int(user_numbers)
            total += user_numbers
            size += 1

            average = (total/size)
            user_numbers = input_file.readline()

            try:
                user_numbers = int(user_numbers)
            except ValueError:
                print("This line is not a number: ")
                print('\t',user_numbers)
                break

    except IOError:
        print("Could not find: " + file_name)

    print("There were", + size, "numbers. ")
    print("The total of all the numbers was:", + total)
    print("The average of the numbers was:", format(average, '.2f'))


main()
