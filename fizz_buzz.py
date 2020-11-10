# Reto para verificar los conocimientos básicos de lógica que se suele aplicar como primer filtro en entrevistas de trabajo.

# Escribe un programa que imprima los números del 1 al 20:
    # Si el númer es múltiplo de 3, escribe Fizz.
    # Si el número es múltiplo de 5, escribe Buzz.
    #Si es múltiplo de 3 y de 5, escribe FizzBuzz.
    # Si no es nunguno de ellos, imprime solamente el número.

i = 1

# while i <= 20:
#     if i % 3 == 0 and i % 5 ==0:
#         print("FizzBuzz")
#     elif i % 3 ==0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)
#     i += 1

for i in range(1, 21):
    if i % 3 == 0 and i % 5 ==0:
        print("FizzBuzz")
    elif i % 3 ==0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
    i += 1