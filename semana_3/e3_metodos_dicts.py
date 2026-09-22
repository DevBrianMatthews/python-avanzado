students = {}

while True:
    print(
        '''
        1. Registrar estudiante (nombre, edad, carrera)
        2. Ver todos los estudiantes
        3. Buscar estudiante por nombre
        4. Actualizar datos de un estudiante
        5. Agregar campo solo si no existe
        0. Salir
        '''
    )

    data = input('Elige el número de la opción: ')

    if data == '1':
        name    = input('Ingresa nombre del estudiante: ')
        age     = input('Ingresa edad del estudiante: ')
        career  = input('Ingresa carrera del estudiante: ')

        students[name] = {'age': age, 'career': career}
        print(students)

    elif data == '2':
        if students:
            for key, value in students.items():
                print(f'{key}: {value}')
        else:
            print('No hay estudiantes aún.')

    elif data == '3':
        name = input('Indica el nombre que quires buscar: ')
        print(f'{ students.get(name, "El estudiante no existe!") }')

    elif data == '4':
        name        = input('A que estudiante quieres actualizar los datos? : ')
        data_key    = input('Que dato quieres actualizar: (age o career) ')
        data_update = input('Escribe el nuevo valor: ')

        if name in students:
            students[name].update({data_key: data_update})
        else:
            print(f'El estudiante {name} no existe')

    elif data == '5':
        key   = input('Que campo deseas agregar? ')
        name  = input('En que estudiante quieres agregar el campo? ')
        valor = input('Ingresa el valor del campo: ')

        if name in students:
            students[name].setdefault(key, valor)
        else:
            print(f'El estudiante {name} no existe')

    elif data == '0':
        break