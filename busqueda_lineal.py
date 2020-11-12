# Ejercicio de Búsqueda líneal del curso POO con Python de Platzi

# Consiste en generar una lista de manera aleatoria de tamaño definido por el usuario.
# El usuario también será responsable de elegir el número a buscar
# Finalmente debe de haber un resultado que defina si el número está en la lista o no está en la lista.

# Búsqueda lineal.

# Peor de los casos O(n)
# Mejor de los casos O(1)
# Caso promedio O(n)




import random

# Generando el algoritmo de búsqueda:
def busqueda_lineal(lista, objetivo):
    match = False #Si encontramos el número objetivo o no

    for elemento in lista:
        if elemento == objetivo:
            match = True
            break    #Con el break no cambia la complejidad algorítmica
    return match

# Generando un algoritmo para la generación de listas y objetivo:

if __name__ == "__main__":
    tamano_lista = int(input('¿De qué tamaño será la lista?: '))
    objetivo = int(input("¿Qué número quieres encontrar?: "))
    lista = [random.randint(0, 101) for i in range(tamano_lista)]

    encontrado = busqueda_lineal(lista, objetivo)
    print(lista)
    # Empleando operadores ternarios --> ejecutar if else en una sola línea:
    print(f'El elemento {objetivo} {"está" if encontrado else "no está"} en la lista') 