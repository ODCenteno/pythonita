"""Finger exercise: Write a program that asks the user to input 10 integers, and then prints the largest odd number that was entered. If no odd number was entered, it should print a message to that effect.

Page: 97 epub book John V. Guttag. “Introduction to Computation and Programming Using Python: With Application to Understanding Data (MIT Press)”. Apple Books. """


askfor = 3
counter = None        # Sentinel value
odd = 0

for n in range(askfor):

    number = int(input('Give me a positive number: ')) # Asking the user for 10 integers
    if number > 0 and number % 2 != 0:
        if counter is None or counter < number:
            counter = number # saves the largest odd entered
            odd += 1
    
if odd > 0:
    print(f'The largest odd number is {counter}')

else:
    print(f'There are no odds in this') # statement for no odds
    
    




