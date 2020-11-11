# Ejercicio asignado desde pywombat.com

# Elementos que más se repiten
# Nivel básico
# Fecha de entrega: 14 nov 2020

# Dado una lista de longitud n, desarrolla un programa el cual cumpla con los siguiente requerimientos.

# El programa debe ser capaz de crear una lista de longitud n, a partir de los datos ingresados por el usuario (vía teclado).
# La longitud de la lista será dada por el usuario.
# Las listas almacenarán, única y exclusivamente, números enteros.
# El programaba debe mostrar en consola el número que más se repite dentro de la lista.
# En caso ningún elemento se encuentre más de una vez en la lista, el programa deberá mostrar el siguiente mensaje en consola.
# Todos los elementos son únicos en tu lista.

# página con 3 formas para revisar duplicados: https://thispointer.com/python-3-ways-to-check-if-there-are-duplicates-in-a-list/

# https://thispointer.com/python-find-duplicates-in-a-list-with-frequency-count-index-positions/

import collections

def run():  

    n_elementos = int(input("Cantidad de elementos: "))
    lista_n = []

    for i in range(n_elementos):
        elementos_en_lista = int(float(input(f'Ingresa los números: ')))
        lista_n.append(elementos_en_lista)
        n_max = (max(set(lista_n), key = lista_n.count))
    if n_max and n_max > 2:
        print(f'El número que más se repite es: {n_max}')
    elif n_max and n_max == 1:
        print(f'Todos los elementos son únicos en la lista')
    else:
        print(f'El número que más se repite es: {n_max}')
    print(f' La Lista tiene {n_elementos} números.')
    print(f' elementos que componen la lista: {lista_n}')   
    # print(lista_n.count)

# list_repe = []

# def check_dup(lista_n):

    # for elem in lista_n:
    #     if lista_n.count(elem) > 1:
    #         list_repe.append(elem)
    #         return True
    #     return False
    
    # result = check_dup(lista_n)

    # if result:
    #     print("La lista tiene duplicados")
    # else:
    #     print("No hay duplicados")


    # for i in range(len(lista_n)):
    #     for j in range(len(lista_n)):
    #         if(lista_n[i] == lista_n[j]):
    #             count = count + 1
    #     if(count > 1):
    #         if(lista_n[i] not in rep):
    #             rep.append(lista_n[i])
    #         count = 0
    # print(rep) 


if __name__ == "__main__":
    run()




