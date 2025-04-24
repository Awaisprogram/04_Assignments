def get_list():
  user_list = []
  i = 1

  while True:
    value = input(f"Enter value {i} (press Enter to stop): ")
    if value == "":
      break
    i += 1
    user_list.append(value)

  print(f"Your list: {user_list}") 


if __name__ == "__main__":
  get_list()