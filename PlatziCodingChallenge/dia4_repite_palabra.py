"""
¿Sabías que para repetir las mismas instrucciones dentro de un programa podemos utilizar for loops o while loops? ¿Sabías que todo lo que puedes hacer con esas loops lo puedes hacer con recursión?
El reto del día de hoy es crear un programa que recibe como parámetro un string y la cantidad de veces que queremos repetir ese string y devuelve una cadena con las repeteciones. ¿El twist? Sólo puedes usar una función recursiva (pro tip: no olvides tu caso base).
"""

# #PlatziCodingChallenge day 4 - By Cemodan

def welcome():                  # Just an entry point to explain the script
    print(f'\n{"*" * 60}')
    
    print(f'''\n\t--- Welcome to the string repeater ---\n\tTo start enter a string\n\t and then set the times it will repeat:''')

# Function that repeats the string using recursion
def recursion(string, repeat_num):      

    if repeat_num == 1:
        return string
    else:
        return string + recursion(string, repeat_num - 1)


if __name__ == "__main__":
    welcome()
    string = input("\n\tEnter a string: ")
    repeat_num = int(input("\n\tHow many times it going to repeat?(Enter an integer): "))
    print(f'\n\tRepeated secuence: {recursion(string, repeat_num)}')