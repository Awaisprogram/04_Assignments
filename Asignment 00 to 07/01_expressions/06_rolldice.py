# This program Simulate rolling two dice, and prints results of each roll as well as the total.

from random import randint

SIDE_NUM = 6

def main():
    die_1 = int(randint(1, SIDE_NUM))
    die_2 = int(randint(1, SIDE_NUM))

    total = die_1 + die_2

    print(f"Dice have {SIDE_NUM} sides")
    print(f"First die: {die_1}")
    print(f"Second die: {die_2}")
    print(f"Total of both die is {total}")

    


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()