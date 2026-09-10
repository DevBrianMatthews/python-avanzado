
task   = []

while True:
    print(
        '''
        === GESTOR DE TAREAS ===

        1.  Agregar tarea al final
        2.  Agregar tarea urgente (va al inicio)
        3.  Completar tarea (elimina la primera)
        4.  Cancelar tarea por nombre
        5.  Ver posición de una tarea
        6.  Ver cuántas veces se repite una tarea
        7.  Ordenar tareas alfabéticamente
        8.  Invertir orden actual
        9.  Ver tareas ordenadas sin modificar la lista
        10. Hacer respaldo de la lista actual
        0.  Salir
        '''
    )
    option = input('— Elije una opción: ')

    if option == '1':
        data = input('Agrega una tarea: ')
        task.append(data)
        print(task)

    elif option == '2':
        data = input('Agrega una tarea urgente: ')
        task.insert(0, data)
        print(task)

    elif option == '3':
        if task:
            task.pop(0)
            print(task)
        else:
            print('No hay tareas a eliminar.')

    elif option == '4':
        name = input('Que tarea quieres eliminar:')
        if name in task:
            task.remove(name)
            print(task)
        else:
            print(f'No existe {name} en la lista')

    elif option == '5':
        tarea = input('Ver posición de la tarea: ')
        if tarea in task:
            print(f'Posición: {task.index(tarea)}')
        else:
            print(f'"{tarea}" no existe en la lista.')

    elif option == '6':
        tarea = input('Cuantas veces se repite la tarea: ')
        print(f'Se repite:  {task.count( tarea )} veces')

    elif option == '7':
        task.sort()
        print(task)

    elif option == '8':
        task.reverse()
        print(task)

    elif option == '9':
        new_list = sorted(task)
        print(new_list)

    elif option == '10':
        backup = task.copy()
        print(backup)

    elif option == '0':
        break
