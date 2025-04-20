# This program adds two numbers

def main()-> None:
  # Get the first number  
  num1 = int(input("Enter first number: "))
  # Get the second number
  num2 = int(input("Enter second number: "))
  # Calculate the sum
  sum = num1 + num2
  # Print the result
  print(f"The sum of {num1} and {num2} is {sum}")
  
if __name__ == '__main__':
  main()