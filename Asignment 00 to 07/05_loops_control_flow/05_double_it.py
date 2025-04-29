def double_it():
    
    curr_value = int(input("Enter a number: "))

    while curr_value < 100:
        curr_value *= 2
        print(curr_value)



if __name__ == '__main__':
    double_it()