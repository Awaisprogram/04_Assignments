MINIMUM_HEIGHT : int = 50

def tall_to_ride():
    user_height = float(input("How tall are you? "))
    if user_height <= MINIMUM_HEIGHT:
        print("You're not tall enough to ride, but maybe next year!")
    else:
        print("You're tall enough to ride!")    


if __name__ == '__main__':
    tall_to_ride()