def get_first_element():
  lst = []
  add = input("Enter a message (press Enter to stop): ")

  while add  != "" :
    lst.append(add)
    add = input("Enter a message (press Enter to stop): ")

  if len(lst) == 0:
    print("The list is empty. You must enter at least one element.")  
  else:
    print("The last element is:", lst[-1])  



if __name__ == "__main__":
  get_first_element()