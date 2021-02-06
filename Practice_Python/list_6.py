"""Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)"""

def palindrome(sentence):
    evaluate = sentence.strip().lower().replace(' ','')

    if evaluate == evaluate[::-1]:
        print("It's a palindrome")
    else:
        print('Not a palindrome')


if __name__ == '__main__':
    palindrome(input('Enter a word or sentence:'))