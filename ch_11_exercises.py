"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free
    Submit your completed file
"""

# TODO 11.1 Introduction to Inheritance
print("=" * 10, "Section 11.1 inheritance", "=" * 10)


# You are going to create a Dwelling class based on the
# Automobile sample from the chapter

# 1) Create the class Dwelling, the __init__ method should accept number_of_rooms, square_feet, floors


class Dwelling:
    def __init__(self, num_room, sqr_feet, floors):
        self.num_room = num_room
        self.sqr_feet = sqr_feet
        self.floors = floors

    # 2) Add mutators for all of the data attributes (number_of_rooms, square_feet, floors)

    def set_num_room(self, num_room):
        self.num_room = num_room

    def set_sqr_feet(self, sqr_feet):
        self.sqr_feet = sqr_feet

    def set_floors(self, floor):
        self.floors = floor

    # 3) Add accessors for all of the data attributes

    def get_num_room(self):
        return self.num_room

    def get_sqr_feet(self):
        return self.sqr_feet

    def get_floors(self):
        return self.floors


house = Dwelling(4, 700, 2)
print('Floors:', house.floors)
print('Floors:', house.get_floors())
print("_______")

# 4) Create the class Single_family_home as a sub class of Dwelling
# The __init__ method should accept number_of_rooms, square_feet, floors, garage_type, yard_size
# -- Call the __init__ of superclass Dwelling and pass the required arguments, remember to include self
# -- Initialize the garage_type and yard_size attributes


class SingleFamilyHome(Dwelling):
    def __init__(self, num_room, sqr_feet, floors, garage_type, yard_size):
        Dwelling.__init__(self, num_room, sqr_feet, floors)
        self.garage_type = garage_type
        self.yard_size = yard_size

# 5) Create the mutator and accessor methods for the garage_type and yard_size attributes

    def set_garage_type(self, garage_type):
        self.garage_type = garage_type

    def get_garage_type(self):
        return self.garage_type

    def set_yard_size(self, yard_size):
        self.yard_size = yard_size

    def get_yard_size(self):
        return self.yard_size

# 6) Demonstrate the Single_family_home class, no need to import because you are in the same file

# 7) Create an object from the Single_family_home class with the following information:
# 6 rooms, 1200 square feet, 1 floor, single car garage, .25 acres

# 8) Display the data using the accessor methods


# 9) Create a main function. Call the main function

def main():
    home = SingleFamilyHome(6, 1200, 1, 'Single Care Garage', '.25 Acres')
    print('Rooms:' , home.get_num_room())
    print('Square Feet:' , home.get_sqr_feet())
    print('Floors:' , home.get_floors())
    print('Garage Type:' , home.get_garage_type())
    print('Yard Size:' , home.get_yard_size())


main()

# TODO 11.2 Polymorphism
print("=" * 10, "Section 11.2 polymorphism", "=" * 10)
# 1) Type in the mammal class from program 11-9, lines 1 - 22

class Mammal:
    def __init__(self, species):
        self.species = species

    def show_species(self):
        print('I am a', self.species)

    def make_sound(self):
        print('Grrrrrr')

# 2) Create a Mouse class as a sub class of the mammal class following the Dog example

class Mouse(Mammal):
    def __init__(self):
        Mammal.__init__(self, 'Mouse')

    def show_species(self):
        print('I am a', self.species)

    def make_sound(self):
        print('Squeak!')

# 3) Create a Bird class as a sub class of the mammal class following the Cat Example

class Bird(Mammal):
    def __init__(self):
        Mammal.__init__(self, 'Bird')

    def show_species(self):
        print('I am a', self.species)

    def make_sound(self):
        print('Chirp!')

def show_mammal_info(creature):
    creature.show_species()
    creature.make_sound()

def main3():
    mammalOBJ = Mammal('Regular Animal')
    mouseOBJ = Mouse()
    birdOBJ = Bird()

    print('Here are some animals and the sounds they make!')
    print()
    show_mammal_info(mammalOBJ)
    print()
    show_mammal_info(mouseOBJ)
    print()
    show_mammal_info(birdOBJ)

main3()


