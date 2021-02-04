"""Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message."""

# Function to ask to the user for a number
def get_number():
    user_number = int(input('Enter a number: '))
    return user_number


# To check if the given number it's odd or even we apply some math
def eval_number(number):
    if number % 2 == 0:
        print(f"The given number it's an even")
    elif number % 2 != 0:
        print(f"The given number  it's an odd")


def check_by_4(number):
    if number % 4 == 0:
        print(f"This number it's a fantanstic four")
    else:
        return


def division_odd(num):
    check = get_number()
    
    if num % check == 0:
        print(f"Number {check} divides evenly to number {num}")
    else:
        print(f"Number {check} dosn't  divide evenly to number {num}")



if __name__ == '__main__':
    number = get_number()
    eval_number(number)
    check_by_4(number)
    num = number
    division_odd(num)