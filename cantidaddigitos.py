# Definir una función la cual nos permita conocer cuantos dígitos posee un número.

# La función debe tener por nombre _cantidaddigitos.
# La función debe poseer el parámetro numero.
# La función debe retornar la cantidad de dígitos del parámetro.
# No es posible utilizar la función str.
# Ejemplos

# >>> cantitdad_digitos(10)
# 2

# >>> cantitdad_digitos(2019)
# 4

# >>> cantitdad_digitos(1234567890)
# 10

def _cantidaddigitos(numero):
    contador = 1

    while numero // 10 > 1:
        contador += 1
    print(contador)







# import math


# def _cantidaddigitos(numero):
#         return 1 + math.floor(math.log10(numero))


# if __name__ == "__main__":
#     numero = int(input("Ingresa un número: "))
#     digitos = _cantidaddigitos(numero)
#     print(digitos)

'''several methods to calculate the length of an integer.
from: https://stackoverflow.com/questions/2189800/how-to-find-length-of-digits-in-an-integer#:~:text=If%20you%20want%20the%20length,len(str(123))%20.
'''

# def libc_size(i): 
#     return libc.snprintf(buf, 100, c_char_p(b'%i'), i) # equivalent to `return snprintf(buf, 100, "%i", i);`

# def str_size(i):
#     return len(str(i)) # Length of `i` as a string

# def math_size(i):
#     return 1 + math.floor(math.log10(i)) # 1 + floor of log10 of i

# def exp_size(i):
#     return int("{:.5e}".format(i).split("e")[1]) + 1 # e.g. `1e10` -> `10` + 1 -> 11

# def mod_size(i):
#     return len("%i" % i) # Uses string modulo instead of str(i)

# def fmt_size(i):
#     return len("{0}".format(i)) # Same as above but str.format