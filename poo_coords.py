# fuente del ejercicio: https://docs.hektorprofe.net/python/programacion-orientada-a-objetos/ejercicios/

# Crea una clase llamada Punto con sus dos coordenadas X e Y.
# Añade un método constructor para crear puntos fácilmente. Si no se reciben una coordenada, su valor será cero.
# Sobreescribe el método string, para que al imprimir por pantalla un punto aparezca en formato (X,Y)
# Añade un método llamado cuadrante que indique a qué cuadrante pertenece el punto, teniendo en cuenta que si X == 0 e Y != 0 se sitúa sobre el eje Y, si X != 0 e Y == 0 se sitúa sobre el eje X y si X == 0 e Y == 0 está sobre el origen.
# Añade un método llamado vector, que tome otro punto y calcule el vector resultante entre los dos puntos.
# (Optativo) Añade un método llamado distancia, que tome otro punto y calcule la distancia entre los dos puntos y la muestre por pantalla. La fórmula es la siguiente: d = sqrt((x2 - x1)**2 + (y2 - y1)**2).

# Crea una clase llamada Rectangulo con dos puntos (inicial y final) que formarán la diagonal del rectángulo.
# Añade un método constructor para crear ambos puntos fácilmente, si no se envían se crearán dos puntos en el origen por defecto.
# Añade al rectángulo un método llamado base que muestre la base.
# Añade al rectángulo un método llamado altura que muestre la altura.
# Añade al rectángulo un método llamado area que muestre el area.

import math

class Punto:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        print(f'P({self.x},{self.y})')

    def cuadrante(self, x, y):  # Método que indica a que cuadrante pertenece el Punto
        self.cuadrante = (x, y)

        if x == 0 and y == 0:
            print(f'El punto {self.cuadrante} está sobre el origen')
        elif x == 0 and y != 0:
            print(f' El punto {self.cuadrante} se situa sobre el eje Y')
        elif x != 0 and y == 0:
            print(f'El punto {self.cuadrante} se situa sobre el eje X')
        elif x > 0 and y > 0:
            print(f' El punto {self.cuadrante} se situa sobre el 1er cuadrante')
        elif x < 0 and y > 0:
            print(f' El punto {self.cuadrante} se situa sobre el 2o cuadrante')
        elif x < 0 and y < 0:
            print(f' El punto {self.cuadrante} se situa sobre el 3er cuadrante')
        elif x > 0 and y < 0:
            print(f' El punto {self.cuadrante} se situa sobre el 4o cuadrante')

    def vector(self):    # Toma dos vectores y calcula el vector resultante entre los dos puntos.
        pass

    def distancia(self):    # toma dos puntos y calcula la distancia entre ellos.
        pass
        d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

class Rectangulo:    # Crea una clase llamada Rectangulo con dos puntos (inicial y final) que formarán la diagonal del rectángulo.

    def __init__(self, inicial=0, final=0):    # Añade un método constructor para crear ambos puntos fácilmente, si no se envían se crearán dos puntos en el origen por defecto.
        self.inicial = inicial
        self.final = final

    def base(self):
        pass

    def altura(self):
        pass

    def area(self):
        pass


if __name__ == "__main__":
    pass






# Experimentación
# Crea los puntos A(2, 3), B(5,5), C(-3, -1) y D(0,0) e imprimelos por pantalla.
# Consulta a que cuadrante pertenecen el punto A, C y D.
# Consulta los vectores AB y BA.
# (Optativo) Consulta la distancia entre los puntos 'A y B' y 'B y A'.
# (Optativo) Determina cual de los 3 puntos A, B o C, se encuentra más lejos del origen, punto (0,0).
# Crea un rectángulo utilizando los puntos A y B.
# Consulta la base, altura y área del rectángulo.