"""
Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number. The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

Extras:

Use binary search.
"""
import random


def number_in_list(used_list, user_number):
    if user_number in used_list:
        print('Short anwers: yes it is')
    else:
        print('No it is not, sorry')


def binary_search(used_list, user_number):
    low = 0
    high = len(used_list) - 1

    while low <= high:
        middle_index = low + (high - low) // 2
        middle_value = used_list[middle_index]
        print(f'Middle Value = {middle_value}')

        if middle_value == user_number:
            return print(f'your number {middle_value} is in the list woha!')
        elif user_number < middle_value:
            high = middle_index - 1

        else:
            low = middle_index + 1
    return print('Not in my binary search, sorry!')
        

def get_list():
    
    the_list = [random.randint(1, 100) for x in range(15)]
    the_list.sort()
    return the_list

def get_user_number():
    print(f'\nLets search some numbers\n To start, please enter a number:')
    try:
        number = int(input(''))
    except TypeError:
        print('Only numbers please')
        get_user_number()
    return number


if __name__ == '__main__':
    used_list = get_list()
    print(used_list)
    user_number = get_user_number()
    just_is = number_in_list(used_list, user_number)
    binary_search(used_list, user_number)
