#This program asks the user for their favorite animal and then prints a message that the user's favorite animal is also the user's favorite animal.

def main()-> None:
#  Get the user's favourite animal
 fav_animal = str(input("What is your favorite animal? "))
#  Print the message with user's favourite animal
 print(f"My favorite animal is also {fav_animal}!")

if __name__ == '__main__':
  main()