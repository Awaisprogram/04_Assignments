def double_number():
  numbers = [1,2,3,4,5]
  for i in range(len(numbers)):
    index = numbers[i]
    numbers[i] = index * 2
  print(numbers)

if __name__ == '__main__':
  double_number()

# 2nd method

def double_numbers(numbers):
  res = []

  for num in numbers:
    res.append(num * 2)
    
  return res
  
if __name__ == '__main__':
  print(double_numbers([1,2,3,4,5]))
