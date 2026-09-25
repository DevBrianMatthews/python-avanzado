
post_tags    = set()
popular_tags = {'Python', 'Js', 'Java','C++', 'PHP'}

while True:
    print(
        '''
        ===== MENU =====
        1. Agregar etiqueta al post
        2. Eliminar etiqueta del post
        3. Ver todas las etiquetas disponibles (union de ambos sets)
        4. Ver etiquetas del post que son populares (intersection)
        5. Ver etiquetas del post que NO son populares (difference)
        0. Salir
        -----------------
        '''
    )
    try:
        num = int(input('Elige una opción: '))
    except ValueError:
        print('Por favor ingresa un numero valido')
        continue

    if num == 1:
        tag = input('Agrega la etiqueta: ')
        post_tags.add(tag)

    elif num == 2:
        tag = input('Elimina la etiqueta: ')
        if tag in post_tags:
            post_tags.discard(tag)
            print(f'Etiqueta {tag} eliminada')
        else:
            print('La etiqueta no existe!')

    elif num == 3:
        if post_tags:
            print(post_tags.union(popular_tags))
        else:
            print('No hay etiquetas!')

    elif num == 4:
        matches = post_tags.intersection(popular_tags)
        if matches:
            print(matches)
        else:
            print('No hay etiquetas populares!')

    elif num == 5:
        print(post_tags.difference(popular_tags))

    elif num == 0:
        break
    else:
        print('Ingresa un número valido dentro de las opciones')