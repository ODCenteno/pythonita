# Aplicando los ciclos For y While para generar una tabla de multiplicar.

tabla = int(input("¿Qué tabla quieres multiplicar?: "))

# i = 1

# while i < 10:
#     print(f'{tabla} x {i} = {tabla*i}')
#     i = i + 1

for i in range(1, 11):
    print(f'{tabla} x {i} = {tabla*i}')