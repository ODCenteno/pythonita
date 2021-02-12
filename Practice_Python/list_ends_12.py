"""Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function."""

import random

def new_list(a):

    b = [a[0], a[-1]]
    print(b)


if __name__ == '__main__':
    a = [5, 10, 15, 20, 25]
    new_list(a)

    random_list = [random.randint(1, 30) for x in range(10)]
    random_list = sorted(random_list)
    print(random_list)
    new_list(random_list)