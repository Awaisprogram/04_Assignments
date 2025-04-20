"""
The program that asks the user for the lengths of the two perpendicular sides of a right triangle and outputs the length of the third side (the hypotenuse) using the Pythagorean theorem!

Formula : BC ** 2 = AB ** 2 + AC ** 2
"""
from math import sqrt  # Import the math library so we can use the sqrt function


def main():
    
    try:
         ab = float(input("Enter the length of AB: "))
         ac = float(input("Enter the length of AC: "))
         hypotenuse =  sqrt(ab ** 2 + ac ** 2)


         print(f"The length of BC (the hypotenuse) is: {hypotenuse}")
    except ValueError:
        print("🚫 Invalid input. Please enter valid numeric values.")     

    
   

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()