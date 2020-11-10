# Programa para preguntar datos a un usuario y decidir si puede votar o no.

edad_votar = 18

nombre = input("¿Cuál es tu nombre?: ")
print(f'muchas gracias {nombre}')


edad = int(input("¿Cuál es tu edad?: \n"))

print(f'{nombre}, tu tienes {edad} años residiendo en el planeta tierra\n')
print("Ojalá sean muchos años más. ¡¡Salud!!\n")

if edad > edad_votar:
    print("Además, ya tienes edad legal para votar\n")
    
elif edad == edad_votar:
    print("¡Felicidades!, ya puedes votar!")
    
else:
    print(f' Dentro de {edad_votar - edad} años podrás votar.')