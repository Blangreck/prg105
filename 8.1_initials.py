def main():

    user_full_name = input('Please type your first, Middle, and Last name. ')
    full_name = user_full_name.split()

    print(full_name)

    first_name = full_name[0][0]
    middle_name = full_name[1][0]
    last_name = full_name[2][0]

    print(first_name.upper(), '.', middle_name.upper(), '.', last_name.upper(), '.')


main()
