"""
Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

  My name is Michele
Then I would see the string:

  Michele is name My
shown back to me."""

def run():
    
    get_str = str.split(input(f'Enter a long string: '))

    print(get_str[::-1])


if __name__ == '__main__':
    run()