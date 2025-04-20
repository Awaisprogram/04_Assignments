# This program finds the perimeter of a triangle

# Method 1

def main():
    print("Find the perimeter of the triangle\n")
    side_1 = float(input("Enter the length of side 1: "))
    side_2 = float(input("Enter the length of side 2: "))
    side_3 = float(input("Enter the length of side 3: "))

    print(f"The perimeter of the traingle is {sum([side_1, side_2, side_3])}")



# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()

# Method 2


def main():
    print("Find the perimeter of the triangle\n")
    sides= []
    for i in range(3):
        side = float(input(f"Enter the length of side_{i+1}: "))
        sides.append(side)
    result = sum(sides)
    print(f"The perimeter of the traingle is {result}")
    



# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()