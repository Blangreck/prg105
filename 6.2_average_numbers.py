def main():
    total = 0
    size = 0
    average = 0

    input_file = open('numbers.txt', 'r')
    numbers = input_file.readline()

    while numbers != "":
        numbers = int(numbers)
        total += numbers
        size += + 1
        average = (total / size)
        numbers = input_file.readline()

    input_file.close()

    print("There's a total of", + size, "numbers.")
    print("The total is", + total)
    print("The average is: ", format(average, ',.2f'))


main()
