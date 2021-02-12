"""
Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

Extra:

Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
"""

import random
import time

def main(user_choice):

    if user_choice == 1:
        weak_pass()
    elif user_choice == 2:
        strong_pass()
    else:
        print(f"That's not a valid option")


def weak_pass():
    tic = time.perf_counter()

    word_list = ['apple', 'plainpass', 'comander', 'happy', 'leon', 'bird', 'main', 'psd']
    weak_password = [random.choice(word_list) for i in range(random.randint(1,3))]
    print(weak_password)
    list_to_string(weak_password, tic)


def strong_pass():
    tic = time.perf_counter()

    chars_list = ['1','2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '?', '¿', '¡', '!', '@', '/', '(', ')', '=', '-', '_', ',', '.', '*', '+', ' ']

    password = random.sample(chars_list[:], 8)
    print(password)
    list_to_string(password, tic)
    

def list_to_string(password, tic):

    str1 = ""
    
    for i in password:
        str1 += i
    print(f"Your new password is: '{str1}'")
    toc = time.perf_counter()
    print(f'Total Time performed is {toc - tic:0.4f}')


if __name__ == '__main__':
    user_choice = int(input(f'Choice password security level:\n\t[1]. Weak Password\n\t[2]. Strong Password\n Enter your selection(1/2): '))
    main(user_choice)