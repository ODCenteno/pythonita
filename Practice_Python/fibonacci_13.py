"""Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.(Hint: The Fibonnaci sequence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)"""


def user_choice():

    ask_user = int(input(f'How many numbers of the secuence do you want to get?: '))
    return ask_user


def make_fib(num):
    
    x = [1]

    if num < 1:
        return 'The number must be positive'

    else:
        for i in range(1, num + 1):
            if i == 1:
                continue
            elif i == 2:
                x.append(1)
                continue
            elif i > 2:
                x.append(x[-2] + x[-1])
        return x 

if __name__=='__main__':
    num = user_choice()

    my_fib = make_fib(num)
    print(my_fib)