# Reto final lanzado por parte de Platzi como parte del Road2Code.

# El reto: Fila de turnos

# Crea una aplicación que permita gestiona una cola con prioridad para brindar orden de atención en un banco u hospital tomando en cuenta los siguientes requerimientos:

# La aplicación tiene un menú con opciones para registrar clientes, solicitar turno, ver la cola de atención y atender clientes.
# Al registrar un cliente se ingresan los siguientes datos: número de identificación, nombres, apellidos, género, edad y tipo de cliente (básico, premium y VIP).
# Pueden existir clientes nuevos para registrar y otros ya registrados.
# Al solicitar turno se debe especificar si el cliente es uno nuevo o ya está registrado, se le pide su ID sea registrado o no, se le asigna un turno según las restricciones de la prioridad y por último se muestra en pantalla su turno.
# Cuando se asignan turnos la cola se modificará según la prioridad de los clientes que vayan llegando. Por ejemplo: si hay 3 clientes básicos y llega un VIP, entonces el VIP pasa al principio de la cola.
# La opción “ver cola” muestra la lista de clientes que no han sido atendidos y en orden de prioridad.
# La opción “atender” muestra los datos del cliente que está al inicio de la cola, lo elimina de la cola de turnos y lo pasa a una lista de clientes atendidos.
# Restricciones de prioridad
# El orden de prioridad de los clientes es: VIP -> Premium -> Básico.
# Si dos clientes del mismo tipo solicitan turno, sele da prioridad al de mayor edad. Si tienen la misma edad se le asigna turno primero al primero en llegar.
# Los clientes nuevos (no registrados) tienen la menor prioridad. Si 2 clientes nuevos de la misma edad solicitan turno, se le da prioridad al primero en llegar.


# Función para desplegar el menú de opciones
def menu():
    print(f'\n{"*" * 50}')
    print(f'\n\t  BANCO LA MORRALLA S.A. de C.V.')
    print(f'\n{"=" * 50}')

    print(f'\n\t       *** Bienvenidx ***\n\n¿Qué tarea desea realizar?\n\n1.-Registrarse en La Morralla\n2.- Solicitar turno\n3.-Ver la cola de atención\n4.- Atender clientes')

    seleccion = int(input("\nElija una de las opciones(1/2/3/4): "))

    if seleccion > 4:
        print(f'Opción incorrecta, elija entre las opciones 1, 2, 3 y 4.')
    elif seleccion < 1:
        print(f'Opción incorrecta, elija entre las opciones 1, 2, 3 y 4.')
    
    else:
        print(f'\n{"*" * 50}')
        return seleccion


# Al registrar un cliente se ingresan los siguientes datos: número de identificación, nombres, apellidos, género, edad y tipo de cliente (básico, premium y VIP).
# Pueden existir clientes nuevos para registrar y otros ya registrados.
def registro():
    pass



# Al solicitar turno se debe especificar si el cliente es uno nuevo o ya está registrado, se le pide su ID sea registrado o no, se le asigna un turno según las restricciones de la prioridad y por último se muestra en pantalla su turno.
# Cuando se asignan turnos la cola se modificará según la prioridad de los clientes que vayan llegando. Por ejemplo: si hay 3 clientes básicos y llega un VIP, entonces el VIP pasa al principio de la cola.
def solicitar_turno():
    pass



# La opción “ver cola” muestra la lista de clientes que no han sido atendidos y en orden de prioridad.
def ver_cola():
    pass





# La opción “atender” muestra los datos del cliente que está al inicio de la cola, lo elimina de la cola de turnos y lo pasa a una lista de clientes atendidos.
# Restricciones de prioridad
# El orden de prioridad de los clientes es: VIP -> Premium -> Básico.
# Si dos clientes del mismo tipo solicitan turno, sele da prioridad al de mayor edad. Si tienen la misma edad se le asigna turno primero al primero en llegar.
# Los clientes nuevos (no registrados) tienen la menor prioridad. Si 2 clientes nuevos de la misma edad solicitan turno, se le da prioridad al primero en llegar.
def atender_clientes():
    pass

if __name__ == "__main__":
    seleccion_usuario = menu()
    