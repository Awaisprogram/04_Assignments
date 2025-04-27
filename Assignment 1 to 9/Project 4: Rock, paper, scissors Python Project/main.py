import random

def play():
  user = input("\nWhat's your choice (s | r | p) : ")
  options = ["s", "r" , "p"]
  if user not in options:
    print("\nInvalid choice. Please choose 's' for Scissors, 'r' for Rock, or 'p' for Paper.")

    return play()
    
  computer = random.choice(options)
  
  results = (f"\nComputer choice is {computer} and you choice is {user}, so")
  print(results)

  if (computer == user):
    return("\nits a tie")
  
  if is_win(user , computer):
    return("\nYou Win")
  
  return("\nYou lost")
  
def is_win(player, opponent):
  if(player == "r" and opponent == "s" ) or\
    (player == "s" and opponent == "p")  or\
    (player == "r" and opponent == "s"):
    return True

print(play())  
  
