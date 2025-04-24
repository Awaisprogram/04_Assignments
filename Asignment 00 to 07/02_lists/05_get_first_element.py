def get_first_element():
  lst = []
  add = input("Enter a message (press Enter to stop): ")

  while add  != "" :
    lst.append(add)
    add = input("Enter a message (press Enter to stop): ")

  if len(lst) == 0:
    print("he list is empty. You must enter at least one element.")  
  else:
    print("The first element is:", lst[0])  



if __name__ == "__main__":
  get_first_element()