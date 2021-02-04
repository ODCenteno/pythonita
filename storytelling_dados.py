"""
Creación de artefacto: story cubes

Reto propio para generar un algoritmo que funcione como unos dados para contar historias. Puede ser el inicio de un proyecto en donde se genere después una aplicación web o una app que nos ayude.

Clase 7 del curso de  cómo preparate profesionalmente para el futuro.
"""

# Número de cubos: 3 o 9 cubos
# Se puede escoger la temática del set de cubos.
# Al recibir el resultado generar un cronómetro con 3 minutos
# Escribir una historia en máximo 560 caracteres con las ideas-palabras. 
# Verificar que las palabras que resultaron de lanzar los dados estén contenidas en la historia contada. y retorne la frase: "Las ideas son una semilla, pronto vaz a florecer". Si no se encuentran las palabras en el texto debe de retornar: "A esta historia le falta leche y palabras"

""" Estrategia para la creación de este algoritmo:

1.- Utilizar POO generando la clase dado que recibe como parámetros sus caras, y como método lanzar dado que regresa una de sus caras.

lanzar dado requier de importar random y elegir.

2. El usuario puede elegir cuantos dados quiere utilizar entre 3 y 9 dados.

4. Debe de desplegarse un texto de bienvenida con la explicación de las reglas del juego y las opciones que se tienen."""

import random

class Dado:

    def __init__(self, cara_1, cara_2, cara_3, cara_4, cara_5, cara_6):
        self.cara_1 = cara_1
        self.cara_2 = cara_2
        self.cara_3 = cara_3
        self.cara_4 = cara_4
        self.cara_5 = cara_5
        self.cara_6 = cara_6

