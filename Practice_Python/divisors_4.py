"""Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)"""


def divisor(user_number):
    divisors = []
    for i in range(1, user_number + 1):
        if user_number % i == 0:
            divisors.append(i)
        else:
            continue
    
    print(divisors)

def new_divisor(user_number):
    
    print([x for x in range(1, user_number + 1) if user_number % x == 0])

if __name__ == '__main__':
    user_number = int(input(f'Enter a number:' ))
    divisor(user_number)
    new_divisor(int(input('Enter a new number: ')))