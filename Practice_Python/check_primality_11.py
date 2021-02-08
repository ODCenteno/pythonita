"""Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions, described below."""

def check_primality(user_number):
    
    if user_number % 2 != 0 and user_number > 0:
        print(f'It is Prime')
    else:
        print(f'It is not prime')


if __name__ == '__main__':
    check_primality(int(input('Enter a number to check if it has primals: ')))