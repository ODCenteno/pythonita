"""Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

Extras:

Write two different functions to do this - one using a loop and constructing a list, and another using sets.
Go back and do Exercise 5 using sets, and write the solution for that in a different function."""


import random

def run(select_method):

    lista = [ random.randint(1, 8) for x in range(10)]
    lista = sorted(lista)
    print(f'>>> The original list is {lista}')

    if select_method == 1:
        looping(lista)
    elif select_method == 2:
        use_sets(lista)
    else:
        print(f'That is not a valid option')


def looping(lista):
    listloop = []
    for num in lista:
        if num in listloop:
            continue
        else:
            listloop.append(num)
    print(listloop)


def use_sets(lista):
    
    listset = list(set(lista))
    print(listset)


if __name__ == '__main__':
    select_method = int(input(f'Please, choose a method to eliminate duplicated items from the list\n\t [1]. Using foor loop\n\t[2]. Using sets\n\tEnter a number to continue(1/2): '))
    run(select_method)