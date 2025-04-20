# This program solve this age-related riddle!

def main()->None:
  # Define the ages of the characters
  anton :int = 21
  beth :int = 6 + anton
  chen :int = 20 + beth
  drew :int = chen + anton
  ethan : int = chen

  # Print the ages of the characters

  print(f"Anton is {anton} years old")
  print(f"Beth is {beth} years old")
  print(f"Chen is {chen} years old")
  print(f"Drew is {drew} years old")
  print(f"Ethan is {ethan} years old")

if __name__ == '__main__':
  main()