#!/usr/bin/python3
import random


def last(number):
    if number >= 0:
        return number % 10
    else:
        if (number % 10) != 0:
            return (number % 10) - 10
        else:
            return 0


def printint(lastdigt):
    print(f"Last digit of {number:d} is {lastdigt:d}", end=" ")
    if lastdigt > 5:
        print("and is greater than 5")
    elif lastdigt == 0:
        print("and is 0")
    elif lastdigt < 6 and lastdigt != 0:
        print("and is less than 6 and not 0")


if __name__ == "__main__":
    number = random.randint(-10000, 10000)
    lastdigt = last(number)
    printint(lastdigt)
