#  This program Ask the user for a number and print its square

def main()->None:
    number = float(input("Enter a number to get its square: "))
    result = number ** 2
    print(f"The square of {number} is {result}")

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()