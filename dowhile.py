#!/usr/bin/env python3

# Created by: Joseph Palermo
# Created on: October 2019
# This program uses a do while loop to get the factorial of integers


def main():
    # this function uses a do while loop to get the factorial of integers

    # variables
    counter = 0
    factorial = 1

    # input
    integer = int(input("Enter an integer: "))
    print("")

    # process & output
    while counter < integer:
        counter = counter + 1
        factorial = factorial*counter

    print("The factorial of", integer, "is {}"
          .format(factorial))


if __name__ == "__main__":
    main()
