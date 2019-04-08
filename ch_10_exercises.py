"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free
    Submit your completed file
"""

import random

# TODO 10.2 modify Coin class to Dice
print("=" * 10, "Section 10.2 Coin class to Dice class", "=" * 10)


class Dice:  # note class names are capitalized
    def __init__(self):
        self.side_up = '1'

    def roll(self):
        randVal = random.randint(1, 6)

        self.side_up = str(randVal)

    def get_side_up(self):
        return self.side_up


def main():
    my_dice = Dice()
    my_dice_two = Dice()
    my_dice.side_up = 5
    print('This side is up, ', my_dice.get_side_up())
    print('This side is up, ', my_dice_two.get_side_up())

    print('I am tossing the coins...')
    my_dice.roll()
    my_dice_two.roll()
    print('This side is up, ', my_dice.get_side_up())
    print('This side is up, ', my_dice_two.get_side_up())


main()
