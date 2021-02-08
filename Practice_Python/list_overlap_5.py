"""Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

Extras:

Randomly generate two lists to test this
Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)"""

import random

def list_overlap(a, b):
    overlaped = []
    for x in a:
        if x in b and x not in overlaped:
            overlaped.append(x)
        else:
            continue
                
    print(f'\nThese are the overlaped numbers from "a" and "b" lists: {sorted(overlaped)}')


def random_lists():

    random_a = [ random.randint(1, 12) for a in range(1, random.randint(1, 12))]
    random_b = [ random.randint(1, 15) for b in range(1, random.randint(1, 15))]

    return random_a, random_b
                
def using_comprehensions(get_random_list):
    
    common_elements = list(set(x for x in get_random_list[0] if x in get_random_list[1]))
    print(f'list of common elements from random lists using comprehensios: {sorted(common_elements)}')

if __name__ == '__main__':
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    list_overlap(a, b)
    get_random_list = random_lists()
    list_overlap(get_random_list[0], get_random_list[1])
    using_comprehensions(get_random_list)

    