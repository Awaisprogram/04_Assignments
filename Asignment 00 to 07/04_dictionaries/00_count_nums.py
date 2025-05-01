def count_num():

  #Empty Dictionary
  number_count = {} 
 
  #continue loop untill user stops
  while True: 

    #get user input
    get_nums = input("Enter a number (press enter to stop): ")

     #stop when the input is empty
    if get_nums == "":
      print("Existing program")
      break 
    #handle type error
    try: 
       get_nums = int(get_nums)
            
    except ValueError:
      print("Value Error! Please enter a valid number.")
      continue 
            
    if get_nums in number_count:
      number_count[get_nums] += 1

    else:
      number_count[get_nums] = 1

  for num, count in number_count.items():
    print(f"{num} appears {count} times.")


if __name__ == '__main__':
  count_num()

        
