def main():
    input_file = open('names.txt', 'r')
    num_lines = 0
    record = input_file.readline()
    record = record.rstrip('\n')

    while record != "":
        print(record)
        num_lines += 1

        record = input_file.readline()
        record = record.rstrip('\n')

    input_file.close()

    print("There are", + num_lines, "names on the list.")


main()
