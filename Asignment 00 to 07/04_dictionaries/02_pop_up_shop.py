def shop():
  fruits = {'apple': 1.5, 'durian': 50, 'jackfruit': 80, 'kiwi': 1, 'rambutan': 1.5, 'mango': 5}
  
   
  total_cost = 0
  for fruit_names in fruits:
    price = fruits[fruit_names]
    bought = int(input(f"Enter the {fruit_names} you wanna buy: "))
    total_cost += (price * bought)

  print(f"Your total cost is {total_cost}")      
if __name__ == '__main__':
  shop()
  