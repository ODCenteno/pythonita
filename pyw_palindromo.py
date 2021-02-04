# Desarrollar un programa el cual nos permita conocer si un string es, o no un palíndromo.

# Un palíndromo es una palabra, o frase que se lee igual de izquierda a derecha que de derecha a izquierda

# El programa debe cumplir con los siguiente requerimientos.

# El programa debe poseer una función llamada palíndromo.
# La función debe poseer como parámetro la variable sentencia.
# La función debe retornar verdadero o falso dependiendo si el parámetro es, o no, un palíndromo.
# Ejemplos

# >>> palindromo('anitalavalatina')
# True

# >>> palindromo('sometamosomatemos')
# True

# >>> palindromo('superpalindromo')
# False
# Ayuda: No es necesario validar, mayusculas, minúsculas, números o espacios.

# Restricciones:

# No es posible implementar ningún método para un
# No es posible importar absolutamente nada.

# def palindromo(sentencia):
#     sentencia = sentencia.strip()
#     sentencia = sentencia.replace(" ", "")
#     sentencia = sentencia.lower()
#     sentencia_reves = sentencia[::-1]
#     if sentencia == sentencia_reves:
#         return True
#     else:
#         return False

# if __name__ == "__main__":
#     sentencia = input("Escribe una frase: ")
#     es_palindromo = palindromo(sentencia)
#     print(es_palindromo)

def palindromo(sentencia):

    sentencia_reves = sentencia[::-1]
    if sentencia == sentencia_reves:
        return True
    else:
        return False

if __name__ == "__main__":
    sentencia = input("Escribe una frase: ")
    es_palindromo = palindromo(sentencia)
    print(es_palindromo)


# Resultado de Pywombat

# def palindromo(sentencia):

#     longitud = len(sentencia)
#     for pos in range(0, longitud // 2):

#         if sentencia[pos] != sentencia[  ((pos - longitud) * - 1) - 1 ]:
#             return False

#     return True
