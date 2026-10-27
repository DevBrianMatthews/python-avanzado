from functools import reduce

products = [
    {'name': 'Manzana', 'price': 1500, 'stock': 10, 'category': 'fruit'},
    {'name': 'Leche',   'price': 3200, 'stock': 0,  'category': 'dairy'},
    {'name': 'Arroz',   'price': 2800, 'stock': 15, 'category': 'grain'},
    {'name': 'Yogur',   'price': 4500, 'stock': 3,  'category': 'dairy'},
    {'name': 'Mango',   'price': 2000, 'stock': 8,  'category': 'fruit'},
    {'name': 'Pan',     'price': 1200, 'stock': 0,  'category': 'grain'},
    {'name': 'Queso',   'price': 6000, 'stock': 5,  'category': 'dairy'},
]
# PUNTO 1
iva = list( map( lambda x: x['price'] * 1.19, products ) )

# PUNTO 2
stock = list( filter( lambda n: n['stock'] > 0,  products ) )

#PUNTO 3
tuple_iva = list( zip( [p['name'] for p in products], iva ) )

# PUNTO 4
index = list( enumerate( [p['name'] for p in products], start=1 ) )

# PUNTO 5
high_price = list( sorted( products, key=lambda x:  x['price'], reverse=True ) )

# PUNTO 6
alpha_name = list( sorted( products, key=lambda x:  x['name'] ) )

# PUNTO 7
total_valor = reduce( lambda acc, x: acc + (x['price'] * x['stock']), products, 0)