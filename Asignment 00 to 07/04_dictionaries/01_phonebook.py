def save_phone_number():
  phone_book = {}

  while True:
    name = str(input("Enter a name: ")).capitalize()
    if name == "":
      break
    number = int(input("Enter a number: "))
    phone_book[name] = number
  return phone_book
  
def display_num(phone_book):
  for name in phone_book:
    print(f"{name} -> {phone_book[name]}")

def lookup_numbers(phone_book):
  while True:
    name = str(input("Enter a name to lookup: ")).capitalize()
    if name == "":
      break
    if name not in phone_book:
      print(f"{name} is not in phonebook")
    else:
      print(f"Number: {phone_book[name]}")     


def main():
  phone_book = save_phone_number()
  display_num(phone_book)
  lookup_numbers(phone_book)

if __name__ == "__main__":
  main()



  