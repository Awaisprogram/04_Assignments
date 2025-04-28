from random import randint

def random_number():
    for _ in range(10):
        value = randint(1 , 100)
        print(value , end=" ")


if __name__ == '__main__':
    random_number()