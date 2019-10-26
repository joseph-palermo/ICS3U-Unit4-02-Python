#!/usr/bin/env python3

# Created by: Joseph Palermo
# Created on: October 2019
# This program uses a do while loop to get the factorial of integers


def main():
    # this function uses a do while loop to get the factorial of integers
    adder = 0
    answer = 0

    # input
    integer = int(input("Enter an integer: "))
    print("")

    # process & output
    while adder <= integer:
        answer = answer + adder
        adder = adder + 1

    print("The answer is {}"
          .format(answer))


if __name__ == "__main__":
    main()
