# This program Converts feet to inches

INCHES_IN_FOOT: int  = 12

def main():
    print("📏 Feet ➡️ Inches Converter\n")
    try:
        feet = float(input("Enter the feet: "))
        inches = feet * INCHES_IN_FOOT
        print(f"\n✅The conversion of {feet} feet is {inches} inches\n")
        print("✨ Thank you for using the converter!\n")

    except ValueError:
        print("🚫 Invalid input. Please enter a valid number.")
                

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()