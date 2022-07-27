
# If else doble one line
m='camelCase'
print("snake_case" if "_" in m else("PascalCase"if m[0].isupper() else"camelCase"))

# if else multiples acciones
l = [5]
if l: rtn = l.pop(); print(f'Last Element deleted {rtn}')
else: print('Empty list')