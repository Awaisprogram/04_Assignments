# This program calculate the number of seconds in a year

DAYS_IN_YEAR = 365
HRS_IN_DAY = 24
MIN_IN_HRS = 60
SEC_IN_MIN = 60

def main():
    print(f"There are {DAYS_IN_YEAR * HRS_IN_DAY * MIN_IN_HRS * SEC_IN_MIN} seconds in a year!")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()