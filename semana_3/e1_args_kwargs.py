"""
E1 - *args, **kwargs, unpacking
Semana 3 - Funciones Avanzadas
"""

title = 'Sales Q1'
data = {'name': 'Tony Stark', 'date': '07/10/2026'}

def generate_report(titulo, *args, **kwargs):
    print(f'=== REPORT: {title} ===')
    print('Items:')
    for i in args:
        print(f'    - {i}')

    print('METADATOS:')
    for key, value in kwargs.items():
        print(f'{key}: {value}')

generate_report(title, 'Apple', 'Pear', 'Pineapple', **data)