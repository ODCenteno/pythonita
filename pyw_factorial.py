# Ejercicio de la Página de Pywombat nivel básico.

# Definir una función la cual nos permita conocer el factorial de un número.

# La función debe tener por nombre factorial.
# La función debe poseer el parámetro valor.
# La función debe retornar el factorial del parámetro.
# La función no debe hacer uso de ningún tipo ciclo.
# Ejemplos.

# >>> factorial(3)
# 6

# >>> factorial(5)
# 120

def factorial(valor):

    if valor == 1:
        return 1
    else:
        return (valor * factorial(valor - 1))

valor = int(input("¿Cuál es el valor a factorizar?: "))
print(factorial(valor))


    