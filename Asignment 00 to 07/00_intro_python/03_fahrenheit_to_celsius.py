# This program converts Fahrenheit to Celsius

def main()-> None:
  # Print the program's purpose
  print("This program converts Fahrenheit to Celsius\n")
  # Get the Fahrenheit temperature
  degrees_fahrenheit = float(input("What is the Fahrenheit temperature? "))
  # Convert Fahrenheit to Celsius
  degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0
  # Print the result
  print(f"The temperature is {degrees_celsius}C")

if __name__ == '__main__':
  main()