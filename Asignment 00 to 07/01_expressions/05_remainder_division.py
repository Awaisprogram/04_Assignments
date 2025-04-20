"""
This program ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.
"""

def main():
    try:
       dividend: int = int(input("🔢 Enter the dividend (number to divide): "))
       divisor: int = int(input("➗ Enter the divisor (number to divide by): "))

       if divisor == 0:
            print("🚫 Error: Division by zero is not allowed.")
            return

       division:int  = dividend // divisor
       remainder:int = dividend % divisor

       print(f"The result of this division is {division} with a remainder of {remainder}") 
       
    except ValueError:
        print("🚫 Invalid input. Please enter valid numeric values.")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()