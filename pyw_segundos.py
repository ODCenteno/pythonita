# Desarrolla un programa el cual nos permita conocer la cantidad de segundos en un día.

# El programa debe mostrar en consola la cantidad de segundos que existen en un día.
# Ejemplo

# $python main.py

# Existen 86400 segundos en un día.



def segundos(day_horas = 24, horas_minutos = 60, minutos_segundos = 60):

    segundos_dia = day_horas * horas_minutos * minutos_segundos
    print(f'Existen {segundos_dia} segundos en un día')

if __name__ == "__main__":
    segundos()
    