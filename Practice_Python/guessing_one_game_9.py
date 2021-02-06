"""Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out."""

import random

def welcome():

    print(f'{"*" * 80}\n\tWelcome to guess the number\n\n- To play write a number between 1 or 9\n- To end the game type "exit"\n')

def ask_for_number():
    get_user_number = input(f'Enter a number to play or "exit" to quit:')
    return get_user_number


def search_number(random_number):

    counter = 0

    while True:
        numbers = ['1', '2', '3','4', '5', '6', '7', '8', '9']
        user_number = ask_for_number()

        if user_number in numbers and int(user_number) == random_number:
            print("You guessed exactly right!")
            counter += 1
        elif user_number in numbers and int(user_number) < random_number:
            print(f'The number was to low')
            counter += 1
        elif user_number in numbers and int(user_number) > random_number:
            print(f'The number was to high')
            counter += 1
        else:
            user_number not in numbers
            return counter


if __name__ == '__main__':
    random_number = random.randint(1, 9)
    print(f'number to guess: {random_number}')
    welcome()
    times_played = search_number(random_number)
    print(f'You played {times_played} times, see you')