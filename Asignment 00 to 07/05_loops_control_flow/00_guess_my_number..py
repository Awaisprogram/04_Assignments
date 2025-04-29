from random import randint

def guess_number():
  secret_number = randint(1,100)

  while True:
    try:
      guess = int(input("Enter a guess: "))
    except:
      print("Please enter a valid number!")
      continue

    if guess == secret_number:
      print(f"Congratulations! You guess the right number: {secret_number}")
      break

    elif guess < secret_number:
      print("Your guess is too low")

    else:
      print("Your guess is too high")    

if __name__ == "__main__":
  guess_number()