def Sum_numbers(numbers:int):
   i = 0

   for num in numbers:
      i += num
   
   return i



if __name__ == '__main__':  
    print(Sum_numbers([1, 2, 3, 4, 5]))  # Call the function with a list of numbers and print the result