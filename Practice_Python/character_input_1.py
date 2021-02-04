"""Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)"""

year = 2021

def ask_user():

    user_name = input("what's your name?: ")
    user_age = int(input("How old are you?: "))

    user_year_born = year - user_age

    return (f'\nHello {user_name}, you will turn 100 years old by {user_year_born + 100}')

def user_number():
    user_repeat_choise = int(input("Give me a number from 1 to 10: "))
    return user_repeat_choise

if __name__ == '__main__':
    one_hundred = ask_user()
    print(one_hundred)
    repeat_num = user_number()
    print(repeat_num)
    print(f'{one_hundred * repeat_num}')
