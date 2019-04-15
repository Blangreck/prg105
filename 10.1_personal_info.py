class PersonalInfo:
    def __init__(self, name, address, age, phone_number):
        self.name = name
        self.address = address
        self.age = age
        self.phone_number = phone_number

    # Setters
    def set_name(self, name):
        self.name = name

    def set_address(self, address):
        self.address = address

    def set_age(self, age):
        self.age = age

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    # Getters
    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_age(self):
        return self.age

    def get_phone_number(self):
        return self.phone_number


def main():
    my_contacts = dict()

    my_contacts[1] = PersonalInfo("Brandon Langreck", "4204 East Drive", 20, "224.828.0724")
    my_contacts[2] = PersonalInfo("Ryan Langreck", "69 South Street", 25, "815.252.6885")
    my_contacts[3] = PersonalInfo("Justin Langreck", "12121 Cooney Drive", 18, "779.713.9919")

    for key, var in my_contacts.items():
        print("Your name is: " + var.get_name())
        print("Your address is: " + var.get_address())
        print("Your age is: " + str(var.get_age()))
        print("Your phone number is: " + var.get_phone_number())
        print("-" * 35)


main()
