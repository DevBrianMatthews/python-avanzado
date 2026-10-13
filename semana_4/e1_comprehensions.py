# EJERCICIO 1
data_celsius = [0, 20, 37, 100]
data_fahrenheit = [(n * 9/5) + 32 for n in data_celsius]

# EJERCICIO 2
data_fahrenheit_30 = [(n * 9/5) + 32 for n in data_celsius if n > 30] 

# EJERCICIO 3
students = ['Ana', 'Luis', 'María']
grades = [8.5, 6.0, 9.2]
new_data = {students[n]: grades[n] for n in range(len(students)) }

# EJERCICIO 4
text = ['python', 'php', 'javascript', 'go', 'java']
new_set = {x for x in text if len(x)> 3}

# EJERCICIO 5
data_nums = [[1,2,3],[4,5,6],[7,8,9]]
new_data_nums = [i for n in data_nums for i in n]

# EJERCICIO 6
total = sum(n ** 2 for n in range(1, 1001))

print(data_fahrenheit)
print(data_fahrenheit_30)
print(new_data)
print(new_set)
print(new_data_nums)
print(total)