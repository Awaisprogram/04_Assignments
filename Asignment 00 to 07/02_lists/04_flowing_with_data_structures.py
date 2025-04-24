def data_flow():
    data = []
    print(f"List before: {data}")

    try:

      for i in range(3):
          message = input(f"Enter a message to copy ({i+1}/3): ")
          data.append(message)
      print(f"List after: {data}")

    except Exception as e:
        print("An unexpected error occurred",str(e))      

    
 

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    data_flow()