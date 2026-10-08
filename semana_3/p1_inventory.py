
inventory = {}

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print('Debe ser un número entero.')

def register_products(*args, **kwargs):
    for name in args:
        inventory[name] = kwargs[name]


while True:
    print(
        '''
        1.  Agregar producto
        2.  Ver todos los productos
        3.  Buscar producto
        4.  Actualizar precio o stock
        5.  Agregar tag a producto
        6.  Eliminar tag de producto
        7.  Buscar productos por tag
        8.  Ver productos ordenados por precio
        9.  Ver productos ordenados por stock
        10. Eliminar producto
        11. Hacer respaldo del inventario
        12. Ver historial de precios de un producto
        13. Ver productos con stock bajo
        14. Registrar múltiples productos de golpe
        0.  Salir
        '''
    )

    data = get_int('Selecciona una opción valida: ')

    if data == 1:

        name  = input('Escribe el nombre del producto: ')
        price = get_int('Escribe el precio del producto: ')
        stock = get_int('Escribe la cantidad de producto: ')
        tags  = input('Escribe las etiquetas del producto separadas por (,): ')

        price_history = []

        tags = set(tags.split(', '))

        inventory.setdefault(
            name, {
                'price':         price,
                'stock':         stock,
                'tags':          tags,
                'price_history': [price]
            }
        )

    elif data == 2:
        if inventory:
            for keys, values in inventory.items():
                print(f'{keys}: {values}')
        else:
            print('Aún no hay productos agregados.')

    elif data == 3:
        name = input('Busca por nombre de producto: ')
        print( inventory.get(name, 'Producto no existe') )

    elif data == 4:
        name = input('Nombre del producto a actualizar: ')

        if name in inventory:
            valor_update = input('Que valor deseas actualizar, precio o stock? ')
            new_valor    = get_int('Cual es el nuevo valor: ')

            if valor_update == 'precio':
                inventory[name].update({'price': new_valor})
                inventory[name]['price_history'].append(new_valor)

            elif valor_update == 'stock':
                inventory[name].update({'stock': new_valor})

            else:
                print('Ese campo no existe')

    elif data == 5:
        name = input('Nombre del producto a agregar tags: ')

        if name in inventory:
            new_tag = input('Escribe la nueva etiqueta: ')
            inventory[name]['tags'].add(new_tag)

    elif data == 6:
        name = input('Nombre del producto a eliminar etiqueta: ')

        if name in inventory:
            del_tag = input('Escribe la etiqueta a eliminar: ')
            inventory[name]['tags'].discard(del_tag)

    elif data == 7:
        search = {input('Escribe el tag del producto: ')}

        for keys, values in inventory.items():
            if values['tags'].intersection(search):
                print(f'{keys}: {values}')

    elif data == 8:
        sorted_inventory = sorted(inventory.items(), key=lambda item: item[1]['price'])
        for name, details in sorted_inventory:
            print(f'{name}: {details}')

    elif data == 9:
        sorted_stock = sorted(inventory.items(), key=lambda item: item[1]['stock'])
        for name, details in sorted_stock:
            print(f'{name}: {details}')

    elif data == 10:
        try:
            name = input('Escribe el producto a eliminar: ')
            print(inventory.pop(name))
        except KeyError:
            print(f'El producto {name} no existe')

    elif data == 11:
        backup = inventory.copy()
        print(backup)

    elif data == 12:
        try:
            name = input('Escribe le producto que quier ver el historial: ')
            print(inventory[name]['price_history'])
        except KeyError:
            print(f'El producto {name} no existe')

    elif data == 13:
        stock_low = []
        for keys, values in inventory.items():
            if values['stock'] < 10:
                stock_low.append((keys, values))

        stock_low.sort(key=lambda item: item[1]['stock'])
        stock_low.reverse()
        print(stock_low)

    elif data == 14:
        name_products = []
        for name in input('Nombres de los productos separados por (,): ').split(','):
            name_products.append(name.strip())
        price_products = list(input('Precios de los productos separados por (,): ').split(','))
        stock_products = list(input('Stock de los productos separados por (,): ').split(','))

        products_data = {}
        for i in range(len(name_products)):
            products_data[name_products[i].strip()] = {
                'price': int(price_products[i].strip()),
                'stock': int(stock_products[i].strip()),
                'tags': set(),
                'price_history': [int(price_products[i].strip())]
            }

        register_products(*name_products, **products_data)

    elif data == 0:
        break
