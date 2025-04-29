AFFIRMATION : str = "I am capable of doing anything I put my mind to."

def main():
    print("Please type the following affirmation exactly:\n")
    print(f"{AFFIRMATION}\n")

    while True:
        user_input = input("Write here: ").strip()
        if user_input == AFFIRMATION:
            print("\nThat's right! 🙂")
            break
        else:
            print(f"\nPlease type the following affirmation:{AFFIRMATION}")



if __name__ == '__main__':
    main()